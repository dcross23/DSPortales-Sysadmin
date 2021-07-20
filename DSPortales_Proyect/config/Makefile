MODULOS := modulosPerl.txt

.PHONY: all
all: config cuotas modulosPerl crontab skel others

.PHONY: config
config:
	rm /etc/hostname
	cp hostname /etc
	chmod 655 /etc/hostname
	rm /etc/motd
	cp motd /etc
	chmod 655 /etc/motd
	@echo "Motd y Hostname configurados\n" >> ../instalacion.log


.PHONY: modulosPerl
modulosPerl:
	apt-get install cpanminus
	while read -r line; do cpanm $$line; done < $(MODULOS)
	apt-get install libdbd-mysql-perl
	apt-get install -y libauthen-simple-pam-perl
	@echo "Modulos Perl instalados\n" >> ../instalacion.log

.PHONY: cuotas
cuotas:
	#Porfavor, añadir "usrquota,grpquota" en fstab antes de nada
	apt-get install quota
	mount -o remount /
	quotacheck -auvgm
	quotaon -uv /
	@echo "Cuotas instaladas\n" >> ../instalacion.log

.PHONY: crontab
crontab:
	crontab cronjobs
	@echo "Crontab instalado\n" >> ../instalacion.log

.PHONY: skel
skel:
	rm -rf /etc/skel
	cp -R skel /etc/skel
	chmod 755 /etc/skel
	@echo "Skel instalado\n" >> ../instalacion.log
	
.PHONY: others
others: 
	apt-get install net-tools
