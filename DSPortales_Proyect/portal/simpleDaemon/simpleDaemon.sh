#!/bin/bash

while true
do 
	/usr/bin/perl /usr/sbin/simpleDaemon/borrarUsuarios.pl
	/usr/bin/perl /usr/sbin/simpleDaemon/cambiarPasswd.pl
	/usr/bin/perl /usr/sbin/simpleDaemon/registrarUsuarios.pl

	sleep 10;
done


