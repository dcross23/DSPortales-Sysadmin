#!/usr/bin/perl

use CGI;
use CGI::Session;
use Authen::Simple::PAM;

my $cgi = new CGI;

my $user = $cgi->param("user");
my $passwd = $cgi->param("passwd");

my $errores = '';

if(!$user or $user !~ /^[a-zA-Z][a-zA-Z0-9_]{3,9}$/){
	$errores = $errores."Usuario invalido - Recuerde: 4 a 10 letras, numeros o _ (ej: usuario_123)</br>";
}

if(!$passwd or $passwd !~ /^[a-zA-Z0-9]{5,20}$/){
	$errores = $errores."Contrasenia invalida - Recuerde: 5 a 20 letras o numeros (ej: abc123abc)</br>";
}



my $pam = Authen::Simple::PAM->new(
        service => 'login'
);


if( $pam->authenticate($user, $passwd) ){
	my $session = new CGI::Session("id:md5", $cgi, {Directory=>"sessions"});
	$session->param("loggedUser", $user);
	$session->expire("+1h");
	$session->flush();

	my $cookie = $cgi->cookie(
    		-name  => 'CGISESSID',
    		-value => $session->id(),
		-expires => '+1h'	
	);

	print $session->header(-cookie=>$cookie);
	print "<meta http-equiv='refresh' content='1; perfil.cgi'>";

}else{
        print $cgi->redirect("/webs/login.html");
}

