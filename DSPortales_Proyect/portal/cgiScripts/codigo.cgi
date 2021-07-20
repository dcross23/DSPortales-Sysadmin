#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Slurp;

my $cgi = new CGI;

my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

my $user = $session->param("user");

if($session->is_expired or !$user){
	$session->delete();
	$session->flush();
	print $cgi->redirect("/webs/remember.html");

}else{
	my $file;
        $file = read_file("webs/code.html");
        print $cgi->header();
        print $file;
}


