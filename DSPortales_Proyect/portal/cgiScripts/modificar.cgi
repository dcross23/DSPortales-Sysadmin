#!/usr/bin/perl

use CGI;
use CGI::Session;
use DBI;
use Email::Send::SMTP::Gmail;
use File::Slurp;
use Crypt::Simple;

my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

my $loggedUser = $session->param("loggedUser");

if($session->is_expired or !$loggedUser){ 
	print $cgi->redirect("/webs/login.html");

}else{
	my $passwd = $cgi->param("passwd");
	my $passwdConf = $cgi->param("passwdConf");
	my $name = $cgi->param("name");
	my $surnames = $cgi->param("surnames");
	my $email = $cgi->param("email");
	my $direction = $cgi->param("direction");

	my $errores = '';
	my $cambios = '';

	my $dsn = "DBI:mysql:database=dsportales;host=localhost";
       	my $dbh = DBI->connect( $dsn , 'admin', '123456');

	if($passwd and $passwd ne ''){
		if($passwd !~ /^[a-zA-Z0-9]{5,20}$/){
			$errores = $errores."Contrasenia invalida - Recuerde: 5 a 20 letras o numeros (ej: abc123abc)</br>";		
		}else{
			if($passwd ne $passwdConf){
				$errores = $errores."Contrasenia no coincide con la confirmacion de contraseña</br>";		
			}else{
        			my $consulta = "insert into cola_modificar values (?,?)";
        			my $query = $dbh->prepare( $consulta );
        			my $cpasswd = encrypt($passwd);
				my $result = $query->execute($loggedUser, $cpasswd);
        			$query->finish();

			 	$cambios = $cambios."Nueva contraseña: $passwd\n";				
			}
		}
	}
	
	if($name and $name ne ''){
		if($name !~ /^[a-zA-Z]+$/){
 			$errores = $errores."Nombre invalido - Recuerde: solo letras</br>";		
		
		}else{
        		my $consulta = "update datos_usuarios set nombre=? where usuario=?";
        		my $query = $dbh->prepare( $consulta );
        		my $result = $query->execute($name, $loggedUser);
        		$query->finish();

			$cambios = $cambios."Nuevo nombre: $name\n";
		}
	}


	if($surnames and $surnames ne ''){
		if($surnames !~ /^[a-zA-Z]+[\ ]?[a-zA-Z]*$/){
			$errores = $errores."Apellidos invalidos - Recuerde: solo letras (apellidos separados por espacio)</br>";
		
		}else{
        		my $consulta = "update datos_usuarios set apellidos=? where usuario=?";
        		my $query = $dbh->prepare( $consulta );
        		my $result = $query->execute($surnames, $loggedUser);
        		$query->finish();

			$cambios = $cambios."Nuevos apellidos: $surnames\n";				
		}
	}
	

	if($email and $email ne ''){
		if(!Email::Valid->address($email)){
        		$errores = $errores."Email invalido - Recuerde: introduzca un email valido (importante)</br>";
		}else{
        		my $consulta = "update datos_usuarios set email=? where usuario=?";
        		my $query = $dbh->prepare( $consulta );
        		my $result = $query->execute($email, $loggedUser);
        		$query->finish();

			$cambios = $cambios."Nuevo email: $email\n";				
		}
	}


	if($direction and $direction ne ''){
		if($direction !~ /^[a-zA-Z0-9\ ]+$/){
        		$errores = $errores."Direccion invalida - Recuerde: letras y numeros y espacios</br>";
		
		}else{
        		my $consulta = "update datos_usuarios set direccion=? where usuario=?";
        		my $query = $dbh->prepare( $consulta );
        		my $result = $query->execute($direction, $loggedUser);
        		$query->finish();

			$cambios = $cambios."Nueva direccion: $direction\n";				
		}
	}

	print $cgi->header();
	
	if(length $errores ){
		print $errores;
	}
	
	if(length $cambios){
        	my $consulta = "select email from datos_usuarios where usuario=?";
        	my $query = $dbh->prepare( $consulta );
        	my $result = $query->execute($loggedUser);
		my @row = $query->fetchrow_array();
		$query->finish();

		if(@row ne 0){
			$email = $row[0];
		
			my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                                 -login=>'dsportalesdys@gmail.com',
                                                 -pass=>'dsportales2021');

        		print "session error: $error" unless ($mail!=-1);

			my $msg = "Se ha modificado su perfil:\n".$cambios;
        		$mail->send(-to=>$email, -subject=>'Perfil actualizado ', -body=>$msg);
        		$mail->bye;

			print "</br> Los nuevos cambios se han mandado a su correo electronico</br>";
		}else{
			print $cambios;
		}

		$dbh->disconnect();

		$session->delete();
		$session->flush();

		print "</br>Vuelva a iniciar sesion por favor</br>";
		print "</br>Sera redireccionado en 5 segundos</br>";
		print "<meta http-equiv='refresh' content='5; /index.html'>";
		exit 0;
	}

	$dbh->disconnect();
	print "</br>Sera redireccionado en 5 segundos</br>";
	print "<meta http-equiv='refresh' content='5; /cgi-bin/cgScripts/perfil.cgi'>";
}
