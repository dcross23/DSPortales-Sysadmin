#!/usr/bin/perl

use DBI;

my $dsn = "DBI:mysql:database=dsportales;host=localhost";
my $dbh = DBI->connect($dsn, 'admin', '123456');
my $consulta = "select * from cola_pag_personales";
my $query = $dbh->prepare( $consulta );
my $result = $query->execute();

while(my @user = $query->fetchrow_array()){
	if(-d "/home/$user[0]/public_html"){
		rename("/home/$user[0]/public_html", "/home/$user[0]/public_html.no");
	}else{
		rename("/home/$user[0]/public_html.no", "/home/$user[0]/public_html");
	}
	
	my $q2 = $dbh->prepare("delete from cola_pag_personales where usuario=?");
	my $r2 = $q2->execute($user[0]);
	$q2->finish();
}

$query->finish();
$dbh->disconnect();



