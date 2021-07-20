
.PHONY: wordpress
wordpress:
	wget https://wordpress.org/latest.tar.gz -P /var/www/html
	tar -xzvf /var/www/html/latest.tar.gz -C /var/www/html
	rm -rf /var/www/html/latest.tar.gz
	cp wp-config.php /var/www/html/wordpress
	chown -R www-data:www-data /var/www/html/wordpress
	mariadb -u root -p -e "source database.sql"



