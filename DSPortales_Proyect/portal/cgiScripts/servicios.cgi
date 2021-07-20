#!/usr/bin/perl
use warnings;
use strict;
use Socket;
use CGI;
use CGI::Session;

sub isActive{
    my ($servicePort) = @_;
   
    my $proto = (getprotobyname('tcp'))[2];
    socket(SOCKET, PF_INET, SOCK_STREAM, $proto);
    
    if(connect( SOCKET, pack_sockaddr_in($servicePort, inet_aton("localhost")))){
        return(" style='color:green;'>ACTIVO &#x2714");
    } else {
       	return(" style='color:red;'>INACTIVO &#x2718");
    }
}


my $cgi = new CGI;
my $session = CGI::Session->load("id:md5", $cgi, {Directory=>"sessions"});

if($session->is_expired or !$session->param("loggedUser")){
	print $cgi->redirect("/webs/login.html");
	exit 0;
}



print $cgi->header();
my $sftp = isActive(21);
my $smtp = isActive(25);
#my $dns = isActive("<br>DNS ..", 53);
my $http = isActive(80);
my $imap = isActive(143);
my $mariadb = isActive(3306);

print '
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">

        <!-- Required meta tags -->

        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1a$">

      	<link rel="stylesheet" href="webs/css/servicios.css"/> 
	
      
  </head>

  <body>
      <table class="table table-info table-striped table-hover table-bordered border-primary">
          <thead>
              <tr>
                  <th scope="col">Servicio</th>
                  <th scope="col">Estado</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <th scope="row">SFTP</th>
                  <td'.$sftp.'</td>
              </tr>
              <tr>
                  <th scope="row">SMTP</th>
                  <td'.$smtp.'</td>
              </tr>
              <tr>
                  <th scope="row">HTTP</th>
                  <td'.$http.'</td>
              </tr>
              <tr>
                  <th scope="row">IMAP</th>
                  <td'.$imap.'</td>
              </tr>
              <tr>
                  <th scope="row">MARIADB</th>
                  <td'.$mariadb.'</td>
              </tr>
          </tbody>
      </table>
  </body>
</html>
';



