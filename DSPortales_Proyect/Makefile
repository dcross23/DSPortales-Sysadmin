
.PHONY: all
all:
	touch instalacion.log
	cd config; make all; cd ..
	cd dnscache; make dnscache; cd ..
	cd MariaDB; make baseDatos; cd ..
	cd simpleDaemon; make simpleDaemon; cd ..
	cd portal; make all; cd ..
	cd MariaDB; make pma; cd ..
	cd correo; make correo; cd ..
	cd sftp; make sftp; cd ..
	cd paginaPersonal; make pagpersonales; cd ..
	cd Tripwire; make tripwire; cd ..
	cd estadisticas; make estadisticas; cd ..
	cd TeamSpeak; make ts; cd ..
	cd wordpress; make wordpress; cd ..

