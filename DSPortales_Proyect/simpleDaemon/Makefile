.PHONY: simpleDaemon
simpleDaemon:
	cp simpleDaemon.service /etc/systemd/system/
	cp -R simpleDaemon /usr/sbin
	chmod ug+x /usr/sbin/simpleDaemon/*
	systemctl enable simpleDaemon.service
	systemctl start simpleDaemon.service
	@echo "SimpleDaemon instalado\n" >> ../instalacion.log
