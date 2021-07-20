.PHONY: ts
ts:
	wget https://files.teamspeak-services.com/releases/server/3.13.5/teamspeak3-server_linux_amd64-3.13.5.tar.bz2
	tar -xjvf teamspeak3-server_linux_amd64-3.13.5.tar.bz2
	rm teamspeak3-server_linux_amd64-3.13.5.tar.bz2
	mkdir /etc/teamspeak
	mv teamspeak3-server_linux_amd64 /etc/teamspeak
	touch /etc/teamspeak/teamspeak3-server_linux_amd64/.ts3server_license_accepted
	cp ts3.service /etc/systemd/system
	chmod 644 /etc/systemd/system/ts3.service
	systemctl enable ts3.service
	systemctl start ts3.service
	@echo "TeamSpeak instalado\n"
