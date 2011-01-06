install:
	install -d /usr/share/cpim
	cp -r conf/* /usr/share/cpim
	install src/cpim /usr/bin
	install src/*.* /usr/bin
	mv /usr/bin/cpim.conf /etc
	install src/helpers/* /usr/bin 
