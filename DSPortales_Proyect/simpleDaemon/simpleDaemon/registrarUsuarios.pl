#!/usr/bin/perl

use warnings;
use strict;

use DBI;
use Linux::usermod;
use Quota;
use File::Path qw(make_path remove_tree);
use File::Copy::Recursive qw(dircopy);
use Crypt::Simple;
use File::Finder;

my $dsn = "DBI:mysql:database=dsportales;host=localhost";
my $dbh = DBI->connect( $dsn , 'admin', '123456');
my $consulta = "select * from registros";
my $query = $dbh->prepare( $consulta );
my $result = $query->execute();

while(my @line = $query->fetchrow_array()){
	my $username = $line[0];
	my $dirhome = "/home/$username";

	#Añadir primero el usuario
	my $passwd = decrypt($line[1]);
	Linux::usermod->add($username, $passwd, undef , undef, undef, $dirhome , "/bin/bash");

	#Añadir el grupo primario del usuario (mismo gid que el uid del usuario)
	my $usercreated = Linux::usermod->new($username);
	Linux::usermod->grpadd($username, $usercreated->get('gid'));
	my $usergroup = Linux::usermod->new($username, 1);
	
	#Crear /home y copiar las cosas de /etc/skel
	make_path($dirhome, { owner => $username, group => $username });
	dircopy("/etc/skel", $dirhome);
	chown($usercreated->get('uid'), $usergroup->get('gid'), File::Finder->in("$dirhome"));
	#chown($usercreated->get('uid'), $usergroup->get('gid'), "$dirhome/public_html.no");	
	#chown($usercreated->get('uid'), $usergroup->get('gid'), "$dirhome/bienvenido.txt");
	
	#Establecer las quotas para ese usuario
	my $quotadev = Quota::getqcarg("/home");
  	Quota::setqlim($quotadev, Linux::usermod->new($username)->get("uid"), 61440, 81920, 0, 0);

	#Añado los datos en la base de datos
	my $q2 = $dbh->prepare("insert into datos_usuarios(usuario, nombre, apellidos, email, direccion) values (?,?,?,?,?)");
	my $r2 = $q2->execute($username, $line[2], $line[3], $line[4], $line[5]);
	$q2->finish();

	#Elimino esa fila de la base de datos
	$q2 = $dbh->prepare("delete from registros where usuario = ?");
	$r2 = $q2->execute($username);
	$q2->finish();
}

$query->finish();
$dbh->disconnect();



