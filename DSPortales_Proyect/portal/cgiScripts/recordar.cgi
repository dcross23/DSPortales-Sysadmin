#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Slurp;
use Linux::usermod;
use DBI;
use Email::Send::SMTP::Gmail;

my $cgi = new CGI;

my $user = $cgi->param("user");

my %users = Linux::usermod->users();

if( exists $users{$user} and $user ne "root"){
	my $session = new CGI::Session("id:md5", $cgi, {Directory=>"sessions"});
	$session->param("user", $user);
	$session->expire("+5m");
	$session->flush();

	my $cookie = $cgi->cookie(
                -name  => 'CGISESSID',
                -value => $session->id(),
                -expires => '+5m'
        );
	
	#Enviar codigo
	my @numeric = (0..9);
	my $code = '';

	for($i=0; $i<6; $i++){
		$code = $code.$numeric[rand @numeric];	
	}
	
	my $dsn = "DBI:mysql:database=dsportales;host=localhost";
        my $dbh = DBI->connect( $dsn , 'admin', '123456');
	my $consulta = "select email from datos_usuarios where usuario=?";
        my $query = $dbh->prepare( $consulta );
        my $result = $query->execute($user);
        my @row = $query->fetchrow_array();
        $query->finish();
	$dbh->disconnect();
        if(@row ne 0){
                 $email = $row[0];
                 my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                           -login=>'david.cruz.garciaa@gmail.com',
                                          -pass=>'garciaaa');

                 print "session error: $error" unless ($mail!=-1);

		 my $msg = "El codigo es: \'$code\'";
                 $mail->send(-to=>$email, -subject=>'Codigo recuperación contrasenia', -body=>$msg);
                 $mail->bye;
                 
        	print $session->header(-cookie=>$cookie);
		$session->param("code", $code); 
		$session->param("email", $email);
		print "<meta http-equiv='refresh' content='1; codigo.cgi'>";
         
	}else{
		$session->delete();
		$session->flush();
		print $cgi->redirect("/webs/remember.html");
	}

}else{
	print $cgi->header();
	print "El usuario no existe</br>";
	print "</br>Sera redireccionado en 3 segundos</br>";
	print "<meta http-equiv='refresh' content='3; /webs/remember.html'>";
}

