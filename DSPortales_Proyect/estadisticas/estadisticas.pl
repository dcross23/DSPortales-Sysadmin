#!/usr/bin/perl

use strict;
use warnings;
use Excel::Writer::XLSX;
use Email::Send::SMTP::Gmail;
use DBI;

# Coger el fichero y cargar en los arrays las columnas que me interesan
my $est1 = 'est1.stats';
my $est2 = 'est2.stats';
my $est3 = 'est3.stats';

my $workbook  = Excel::Writer::XLSX->new( 'estadisticas.xlsx' );
die "Problems creating new Excel file: $!" unless defined $workbook;

#Estadisticas 1
my $worksheet = $workbook->add_worksheet();
open my $info, $est1 or die "Could not open $est1: $!";

my @nombres;
my @horas;

while( my $line = <$info>)  {   
	chomp $line;
	my @data = split / /, $line;
	@data = grep($_, @data);
	$data[0] =~ s/\s+//g;	
	push(@nombres, $data[0]);
	$data[1] =~ s/\s+//g;	
	push(@horas, $data[1]);
}

close $info;

 
# Add the worksheet data the chart refers to.
my $est1data = [
    [ 'Nombre', @nombres ],
    [ 'Horas',  @horas ]
];
 
$worksheet->write( 'A1', $est1data );

my $chart     = $workbook->add_chart( type => 'pie', embedded => 1 );

# Configure the chart.
$chart->add_series(
    categories => [ 'Sheet1', 1, 60, 0, 0 ],
    values     => [ 'Sheet1', 1, 60, 1, 1 ],
);

$chart->set_title( name => 'Top 3 usuarios mas activos' );
$chart->set_style( 10 );
$chart->set_size( width => 800, height => 600 );

$worksheet->insert_chart( 'C2', $chart, 20, 20 );



#Estadisticas 2
$worksheet = $workbook->add_worksheet();
open my $info2, $est2 or die "Could not open $est2: $!";

my @nombres2;
my @porc;

while( my $line = <$info2>)  {   
	chomp $line;
	my @data = split / /, $line;
	@data = grep($_, @data);
	$data[8] =~ s/\s+//g;	
	push(@nombres2, $data[8]);
	$data[1] =~ s/\s+//g;
	chop($data[1]);
	push(@porc, $data[1]);
}

close $info2;

 
# Add the worksheet data the chart refers to.
my $est2data = [
    [ 'Nombre', @nombres2 ],
    [ 'Horas',  @porc ]
];
 
$worksheet->write( 'A1', $est2data );

$chart = $workbook->add_chart( type => 'pie', embedded => 1 );

# Configure the chart.
$chart->add_series(
    categories => [ 'Sheet2', 1, 60, 0, 0 ],
    values     => [ 'Sheet2', 1, 60, 1, 1 ],
);

$chart->set_title( name => 'Top 5 comandos mas utilizados' );
$chart->set_style( 10 );
$chart->set_size( width => 800, height => 600 );

$worksheet->insert_chart( 'C2', $chart, 20, 20 );


#Estadisticas 3
$worksheet = $workbook->add_worksheet();
open my $info3, $est3 or die "Could not open $est3: $!";

my @nombres3;
my @tiempo;

while( my $line = <$info3>)  {   
	chomp $line;
	my @data = split / /, $line;
	@data = grep($_, @data);
	$data[8] =~ s/\s+//g;	
	push(@nombres3, $data[8]);
	$data[4] =~ s/\s+//g;
	chop($data[4]);
	chop($data[4]);
	push(@tiempo, $data[4]);
}

close $info3;

 
# Add the worksheet data the chart refers to.
my $est3data = [
    [ 'Nombre', @nombres3 ],
    [ 'Tiempo cpu',  @tiempo ]
];
 
$worksheet->write( 'A1', $est3data );

$chart = $workbook->add_chart( type => 'pie', embedded => 1 );

# Configure the chart.
$chart->add_series(
    categories => [ 'Sheet3', 1, 60, 0, 0 ],
    values     => [ 'Sheet3', 1, 60, 1, 1 ],
);

$chart->set_title( name => 'Top 5 comandos que mas cpu han consumido' );
$chart->set_style( 10 );
$chart->set_size( width => 800, height => 600 );

$worksheet->insert_chart( 'C2', $chart, 20, 20 );


$workbook->close();

# Enviarme esta gráfica por correo
my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                                 -login=>'dsportalesdys@gmail.com',
                                                 -pass=>'dsportales2021');
 
print "session error: $error" unless ($mail!=-1);
 
my $msg = 'Os adjuntamos el informe semanal de estadisticas';

my $dsn = "DBI:mysql:database=dsportales;host=localhost";
my $dbh = DBI->connect( $dsn , 'admin', '123456');
my $consulta = "select * from datos_usuarios";
my $query = $dbh->prepare( $consulta );
my $result = $query->execute();
while(my @line = $query->fetchrow_array()){
	my $email = $line[3];
	$mail->send(-to=>$email, -subject=>'Estadisticas', -body=>$msg,
           	 -attachments=>'estadisticas.xlsx');
 }
$mail->bye;

unlink  "estadisticas.xlsx";
unlink  "est1.stats";
unlink  "est2.stats";
unlink  "est3.stats";


