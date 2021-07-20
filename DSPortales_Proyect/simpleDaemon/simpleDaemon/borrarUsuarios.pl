#!/usr/bin/perl

use DBI;
use Linux::usermod;
use File::Path qw(make_path remove_tree);

my $dsn = "DBI:mysql:database=dsportales;host=localhost";
my $dbh = DBI->connect($dsn, 'admin', '123456');
my $consulta = "select * from cola_eliminar";
my $query = $dbh->prepare( $consulta );
my $result = $query->execute();

my %users = Linux::usermod->users();
my %groups = Linux::usermod->grps();

while(my @user = $query->fetchrow_array()){
	if( exists $users{$user[0]} and $user[0] ne "root"){
		#Eliminar usuario, grupo principal y su /home
		Linux::usermod->del($user[0]);
		Linux::usermod->grpdel($user[0]) if exists $groups{$user[0]};
		remove_tree("/home/$user[0]");
		
		#Eliminar datos de las bases de datos
		my $c2 = "delete from datos_usuarios where usuario=?";
		my $q2 = $dbh->prepare( $c2 );
		my $r2 = $q2->execute( $user[0] );
		$q2->finish();
	}

	my $c3 = "delete from cola_eliminar where usuario=?";
	my $q3 = $dbh->prepare( $c3 );
	my $r3 = $q3->execute( $user[0] );
	$q3->finish();
}

$query->finish();
$dbh->disconnect();
