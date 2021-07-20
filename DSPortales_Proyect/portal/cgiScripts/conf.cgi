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
	my $file;
	$file = read_file("webs/config.html");
	
	print $cgi->header();
	print $file;
}
