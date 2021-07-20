
.PHONY: all
all: baseDatos pma


.PHONY: baseDatos
baseDatos:
	apt-get install mariadb-client mariadb-server
	mysql_secure_installation
	mariadb -u root -p -e "source installer.sql"
	@echo "Bases de datos instaladas\n" >> ../instalacion.log

.PHONY: pma
pma:
	apt-get install php libapache2-mod-php php-mysql php-xml php-gd php-json php-curl php-mbstring php-zip
	wget https://files.phpmyadmin.net/phpMyAdmin/5.1.1/phpMyAdmin-5.1.1-all-languages.zip
	unzip phpMyAdmin-5.1.1-all-languages.zip
	rm phpMyAdmin-5.1.1-all-languages.zip
	mv phpMyAdmin-5.1.1-all-languages /var/www/html/pma
	chown -R www-data:www-data /var/www/html/pma
	chmod 755 /var/www/html/pma
	@echo "PhpMyAdmin instalado\n" >> ../instalacion.log
