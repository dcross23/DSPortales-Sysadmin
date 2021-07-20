#!/usr/bin/perl

use DBI;
use Linux::usermod;
use Crypt::Simple;

my $dsn = "DBI:mysql:database=dsportales;host=localhost";
my $dbh = DBI->connect( $dsn , 'admin', '123456');
my $consulta = "select * from cola_modificar";
my $query = $dbh->prepare( $consulta );
my $result = $query->execute();

my %users = Linux::usermod->users();

while(my @row = $query->fetchrow_array()){
	if( exists $users{$row[0]} and $user ne "root" ){
		my $user = Linux::usermod->new($row[0]);
		my $passwd = decrypt($row[1]);
		$user->set('password', $passwd);
	}

	my $q2 = $dbh->prepare("delete from cola_modificar where usuario=?");
	my $r2 = $q2->execute($row[0]);
	$q2->finish();
}

$query->finish();
$dbh->disconnect();

