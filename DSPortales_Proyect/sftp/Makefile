
.PHONY: sftp 
sftp:
	apt-get install vsftpd
	systemctl start vsftpd
	rm /etc/vsftpd.conf
	cp vsftpd.conf /etc
	chmod 755 /etc/vsftpd.conf
	systemctl restart vsftpd
	ln -s /var/log/vsftpd.log /logsAdmin/logins.log
	@echo "SFTP instalado\n" >> ../instalacion.log	
