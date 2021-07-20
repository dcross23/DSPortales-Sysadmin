
.PHONY: all
all: portal webs logs

.PHONY: portal
portal:
	apt-get install apache2
	systemctl start apache2
	apt-get install apache2-suexec-custom
	a2enmod cgi
	a2enmod suexec
	systemctl restart apache2
	useradd -r -d /nonexistent -s /usr/sbin/nologin suadmin
	usermod -a -G shadow suadmin
	groupadd -r administrators
	adduser admin
	usermod -a -G administrators admin
	rm /etc/apache2/sites-available/000-default.conf
	cp 000-default.conf /etc/apache2/sites-available
	chmod 644 /etc/apache2/sites-available/000-default.conf
	rm /etc/apache2/suexec/www-data
	cp www-data /etc/apache2/suexec
	chmod 644 /etc/apache2/suexec/www-data
	systemctl restart apache2
	@echo "Portal instalado\n" >> ../instalacion.log

.PHONY: webs
webs:
	rm -r /var/www/html
	cp -R html /var/www
	chown -R www-data:www-data /var/www/html/*
	chmod a+x /var/www/html
	chmod a+x /var/www/html/webs
	cp -R cgiScripts /usr/lib/cgi-bin
	chmod a+x /usr/lib/cgi-bin/cgiScripts
	chown -R suadmin:suadmin /usr/lib/cgi-bin/cgiScripts
	chmod go+rx /usr/lib/cgi-bin/cgiScripts/webs
	chmod -R 700 /usr/lib/cgi-bin/cgiScripts/*
	chmod 755 /usr/lib/cgi-bin/cgiScripts/webs
	chmod -R 755 /usr/lib/cgi-bin/cgiScripts/webs/css
	chmod -R 755 /usr/lib/cgi-bin/cgiScripts/webs/images
	systemctl restart apache2
	@echo "Webs instaladas\n" >> ../instalacion.log


.PHONY: logs
logs:
	mkdir /logsAdmin
	@echo "Logs instalados\n" >> ../instalacion.log
