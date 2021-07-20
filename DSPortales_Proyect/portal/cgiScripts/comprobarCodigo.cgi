#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Slurp;
use Email::Send::SMTP::Gmail;
use DBI;
use Crypt::Simple;

my $cgi = new CGI;

my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

my $user = $session->param("user");
my $email = $session->param("email");
my $code = $session->param("code");

if($session->is_expired or !$user or !$email or !$code){
	print $cgi->redirect("/webs/remember.html");

}else{
	$insertedCode = $cgi->param("code");
	print $cgi->header();

	if($insertedCode and $code eq $insertedCode){
		#Generar contaseña
		my @alphanumeric = ('a'..'z', 'A'..'Z', 0..9);   
		my $randPasswd = '';

        	for($i=0; $i<10; $i++){
        	        $randPasswd = $randPasswd.$alphanumeric[rand @alphanumeric];
        	}
	
		my $dsn = "DBI:mysql:database=dsportales;host=localhost";
        	my $dbh = DBI->connect( $dsn , 'admin', '123456');
        	my $consulta = "insert into cola_modificar values (?,?)";
        	my $query = $dbh->prepare( $consulta );
        	my $cpasswd = encrypt($randPasswd);
		my $result = $query->execute($user, $cpasswd);
        	$query->finish();
        	$dbh->disconnect();


		my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                           -login=>'david.cruz.garciaa@gmail.com',
                                           -pass=>'garciaaa');

                print "session error: $error" unless ($mail!=-1);

                my $msg = "La nueva contraseña es: \'$randPasswd\'\nSe recomienda iniciar sesion y cambiarla";
                $mail->send(-to=>$email, -subject=>'Nueva contrasenia', -body=>$msg);
                $mail->bye;
		
		print "Se ha enviado los nuevos datos a su correo electronico</br>";
		print "</br>Sera redireccionado en 5 segundos</br>";
        	print "<meta http-equiv='refresh' content='5; /index.html'>";

	}

	$session->delete();
	$session->flush();
}


