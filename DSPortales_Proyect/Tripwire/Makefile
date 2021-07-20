
.PHONY: tripwire
tripwire:
	apt-get install tripwire
	rm /etc/tripwire/twpol.txt
	cp twpol.txt /etc/tripwire/
	chmod 655 /etc/tripwire/twpol.txt
	tripwire -m i
	tripwire -m c
	@echo "Tripwire instalado\n"
