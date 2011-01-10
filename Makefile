install:
	install -d /usr/share/copim
	cp -r conf/* /usr/share/copim
	install src/copim /usr/bin
	install src/*.* /usr/bin
	mv /usr/bin/copim.conf /etc
	install src/helpers/* /usr/bin 
