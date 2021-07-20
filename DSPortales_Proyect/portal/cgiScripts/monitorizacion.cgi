#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use CGI::Session;
use Sys::Statistics::Linux;
use Sys::Statistics::Linux::DiskUsage;
use Excel::Writer::XLSX;
use Email::Send::SMTP::Gmail;
use Filesys::Df;


my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory => "sessions"});

if($session->is_expired){
	print $cgi->redirect("/webs/login.html");
	exit 0;
}


my $lxs = Sys::Statistics::Linux->new( cpustats => 1,
				       memstats => 1
	);

sleep(1);


my $stat = $lxs->get;
my $cpu = $stat->cpustats->{cpu};
my $mem = $stat->memstats;
my $disk = df("/");  

my @cpuNames = ("usuarios", "sistema", "nice", "IO", "inactivo");
my @cpuPorc = ($cpu->{user}, $cpu->{system}, $cpu->{nice}, $cpu->{iowait}, $cpu->{idle});

my @memNames = ("usada", "libre");
my $memUsada = $mem->{memusedper};
my @memPorc = ($memUsada, 100-$memUsada);

my @diskNames = ("usado (mb)", "libre(mb)");
my @diskUsage = ($disk->{used}/1024, $disk->{bfree}/1024);


# Crear una grafica circular con los datos
my $workbook  = Excel::Writer::XLSX->new( 'monitorizacion.xlsx' );
die "Problems creating new Excel file: $!" unless defined $workbook;


#Hoja para estadisticas de cpu
my $worksheet = $workbook->add_worksheet();
 
my $cpudata = [
    [ 'Nombre', @cpuNames ],
    [ '%',   @cpuPorc ]
];
 
$worksheet->write( 'A1', $cpudata );
my $chart = $workbook->add_chart( type => 'pie', embedded => 1 );
$chart->add_series(
    categories => [ 'Sheet1', 1, 60, 0, 0 ],
    values     => [ 'Sheet1', 1, 60, 1, 1 ],
);

$chart->set_title( name => 'Uso de CPU' );
$chart->set_style( 10 );
$chart->set_size( width => 600, height => 600 );

$worksheet->insert_chart( 'C2', $chart, 20, 20 );



#Hoja para estadisticas de memoria
$worksheet = $workbook->add_worksheet();

my $memdata = [
    [ 'Nombre', @memNames ],
    [ '%',   @memPorc ]
];

$worksheet->write( 'A1', $memdata );

$chart = $workbook->add_chart( type => 'pie', embedded => 1 );

# Configure the chart.
$chart->add_series(
    categories => [ 'Sheet2', 1, 60, 0, 0 ],
    values     => [ 'Sheet2', 1, 60, 1, 1 ],
);

$chart->set_title( name => 'Uso de Memoria' );
$chart->set_style( 10 );
$chart->set_size( width => 600, height => 600 );

$worksheet->insert_chart( 'C2', $chart, 20, 20 );


#Hoja para estadisticas de disco
$worksheet = $workbook->add_worksheet();
 
my $diskdata = [
    [ 'Nombre', @diskNames ],
    [ 'Valor',  @diskUsage ]
];
 
$worksheet->write( 'A1', $diskdata );
$chart = $workbook->add_chart( type => 'pie', embedded => 1 );
$chart->add_series(
    categories => [ 'Sheet3', 1, 60, 0, 0 ],
    values     => [ 'Sheet3', 1, 60, 1, 1 ],
);

$chart->set_title( name => 'Uso de Disco' );
$chart->set_style( 10 );
$chart->set_size( width => 600, height => 600 );

$worksheet->insert_chart( 'C2', $chart, 20, 20 );

$workbook->close();



# Enviarme las gráficas por correo
my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                                 -login=>'dsportalesdys@gmail.com',
                                                 -pass=>'dsportales2021');
 
print "session error: $error" unless ($mail!=-1);
 
my $msg = "Monitorizacion del sistema:";
$mail->send(-to=>'dsportalesdys@gmail.com', -subject=>'Monitorizacion del sistema', -body=>$msg,
            -attachments=>'monitorizacion.xlsx');
 
$mail->bye;

unlink "monitorizacion.xlsx";

print $cgi->redirect("perfil.cgi")

