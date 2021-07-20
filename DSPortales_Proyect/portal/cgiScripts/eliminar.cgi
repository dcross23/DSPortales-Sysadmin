#!/usr/bin/perl


use CGI;
use CGI::Session;
use File::Slurp;
use DBI;

my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

my $loggedUser = $session->param("loggedUser");

if($session->is_expired or !$loggedUser){ 
	print $cgi->redirect("/webs/login.html");

}else{
	my $dsn = "DBI:mysql:database=dsportales;host=localhost";
        my $dbh = DBI->connect( $dsn , 'admin', '123456');
        my $consulta = "insert into cola_eliminar values (?)";
        my $query = $dbh->prepare( $consulta );
        my $result = $query->execute($loggedUser);
        $query->finish();
        $dbh->disconnect();

	$session->delete();
	$session->flush();

	print $cgi->header();
	print "Su cuenta ha sido eliminada correctamente</br>";
	print "</br>Sera redireccionado en 5 segundos</br>";
	print "<meta http-equiv='refresh' content='5; /index.html'>";
}
