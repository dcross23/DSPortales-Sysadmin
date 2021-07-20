#!/usr/bin/perl


use CGI;
use CGI::Session;
use File::Slurp;
use Linux::usermod;

my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

my $loggedUser = $session->param("loggedUser");

if($session->is_expired or !$loggedUser){ 
	$session->delete();
	$session->flush();
	print $cgi->redirect("/webs/login.html");

}else{
	my $file;
	my $group = Linux::usermod->new("administrators", 1);
	my @admins = split(",", $group->get("users"));
	
	if(grep( /^$loggedUser$/, @admins) ){
		$file = read_file("webs/admin.html");
	}else{
		$file = read_file("webs/user.html");
	}
	
	print $cgi->header();
	print $file;
}
