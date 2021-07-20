#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Slurp;

my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

my $loggedUser = $session->param("loggedUser");

if($session->is_expired or !$loggedUser){ 
	print $cgi->redirect("/webs/login.html");

}else{
	$session->delete();
	$session->flush();
	print $cgi->header();
	print "Su sesion ha finalizado</br>";
	print "</br>Sera redireccionado en 3 segundos</br>";
	print "<meta http-equiv='refresh' content='3; /index.html'>";
}
