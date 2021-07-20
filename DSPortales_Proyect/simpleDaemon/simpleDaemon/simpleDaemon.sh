#!/bin/bash

while true
do 
	/usr/bin/perl /usr/sbin/simpleDaemon/borrarUsuarios.pl
	/usr/bin/perl /usr/sbin/simpleDaemon/cambiarPasswd.pl
#	/usr/bin/perl /usr/sbin/simpleDaemon/registrarUsuarios.pl
	/usr/bin/perl /usr/sbin/simpleDaemon/actDesPagPersonales.pl
	sleep 6;
done


