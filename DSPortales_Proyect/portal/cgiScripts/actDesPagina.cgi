#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Path qw(make_path);
use DBI;

my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

if($session->is_expired or !$session->param("loggedUser")){
	print $cgi->redirect("/webs/login.html");
	exit 0;
}

my $loggedUser = $session->param("loggedUser");

my $dsn = "DBI:mysql:database=dsportales;host=localhost";
my $dbh = DBI->connect( $dsn , 'admin', '123456');
my $consulta = "insert into cola_pag_personales values (?)";
my $query = $dbh->prepare( $consulta );
my $result = $query->execute($loggedUser);

$query->finish();
$dbh->disconnect();


print $cgi->header();

if(-d "/home/$loggedUser/public_html/"){
	print "HA DESACTIVADO SU PAGINA WEB<br>";
	print "Para volver a activarla, vuelta a pulsar el boton<br>";
}else{
	print "HA ACTIVADO SU PAGINA WEB<br>";
	print "Para desactivarla, vuelta a pulsar el boton<br>";
}

print "</br>Sera redireccionado en 5 segundos</br>";
print "<meta http-equiv='refresh' content='5; perfil.cgi'>";

