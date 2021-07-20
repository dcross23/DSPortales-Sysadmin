#!/usr/bin/perl

use CGI;
use DBI;
use Email::Valid;
use Email::Send::SMTP::Gmail;
use Crypt::Simple;
use Linux::usermod;

my $cgi = new CGI;

my $user = $cgi->param("user");
my $passwd = $cgi->param("passwd");
my $name = $cgi->param("name");
my $surnames = $cgi->param("surnames");
my $email = $cgi->param("email");
my $direction = $cgi->param("direction");


my $errores = '';

if(!$user or $user !~ /^[a-zA-Z][a-zA-Z0-9_]{3,9}$/){
	$errores = $errores."Usuario invalido - Recuerde: 4 a 10 letras, numeros o _ (ej: usuario_123)</br>";
}

if(!$passwd or $passwd !~ /^[a-zA-Z0-9]{5,20}$/){
	$errores = $errores."Contrasenia invalida - Recuerde: 5 a 20 letras o numeros (ej: abc123abc)</br>";
}

if(!$name or $name !~ /^[a-zA-Z]+$/){
	$errores = $errores."Nombre invalido - Recuerde: solo letras</br>";
}

if(!$surnames or $surnames !~ /^[a-zA-Z]+[\ ]?[a-zA-Z]*$/){
	$errores = $errores."Apellidos invalidos - Recuerde: solo letras (apellidos separados por espacio)</br>";
}

if(!$email or !Email::Valid->address($email)){
	$errores = $errores."Email invalido - Recuerde: introduzca un email valido (importante)</br>";
}

if(!$direction or $direction !~ /^[a-zA-Z0-9\ ]+$/){
	$errores = $errores."Direccion invalida - Recuerde: letras y numeros y espacios</br>";
}


#Comprobar si el usuario esta creado o no
my %users = Linux::usermod->users();
if(exists($users{$user})){
	$errores = $errores. "<br> USUARIO YA EXISTENTE!!!! UTILICE OTRO USUARIO<br>";
}


print $cgi->header();
if(length $errores){
	print $errores;

}else{
	#Guardar en la base de datos de registros
	my $dsn = "DBI:mysql:database=dsportales;host=localhost";
	my $dbh = DBI->connect( $dsn , 'admin', '123456');
	my $consulta = "insert into registros values (?,?,?,?,?,?)";
	my $query = $dbh->prepare( $consulta );
	
	my $cpasswd = encrypt($passwd);
	my $result = $query->execute($user, $cpasswd, $name, $surnames, $email, $direction);

	$query->finish();
	$dbh->disconnect();

	#Enviar datos por correo electronico
	my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                                 -login=>'dsportalesdys@gmail.com',
                                                 -pass=>'dsportales2021');
 
	print "session error: $error" unless ($mail!=-1);
 
	my $msg = "Bienvenido, estos son tus datos:\n
		   - Usuario:$user\n
		   - Constrasenia:$passwd\n
		   - Nombre:$name\n
		   - Apellidos:$surnames\n
		   - Email:$email\n
		   - Direccion:$direction\n";

	$mail->send(-to=>$email, -subject=>'Bienvenido a DSPortales ', -body=>$msg);
	$mail->bye;

	print "Ha sido registrado correctamente, hemos mandado sus datos a su correo electronico</br>";
}

print "</br>Sera redireccionado en 5 segundos</br>";
print "<meta http-equiv='refresh' content='5; /index.html'>";
