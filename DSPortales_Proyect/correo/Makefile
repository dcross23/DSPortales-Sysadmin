
.PHONY: correo
correo:
	apt-get install postfix
	systemctl start postfix
	rm /etc/postfix/main.cf
	cp main.cf /etc/postfix
	chown root:root /etc/postfix/main.cf
	chmod 655 /etc/postfix/main.cf
	systemctl restart postfix
	apt-get install dovecot-imapd
	systemctl start dovecot
	apt-get install roundcube
	rm /etc/roundcube/config.inc.php
	cp config.inc.php /etc/roundcube
	chown root:www-data /etc/roundcube/config.inc.php
	chmod 650 /etc/roundcube/config.inc.php
	cp logo.jpg /usr/share/roundcube
	chmod 655 /usr/share/roundcube/logo.jpg
	cp logoemail.png /usr/share/roundcube
	chmod 655 /usr/share/roundcube/logoemail.png
	ln -s /usr/share/roundcube /var/www/html/correo
	chown www-data:www-data /var/www/html/correo
	systemctl restart postfix
	systemctl restart dovecot
	@echo "Correo instalado\n" >> ../instalacion.log
