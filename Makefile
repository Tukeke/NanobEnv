DPATH="/usr/"
all: install

install-common:
	install -d $(DESTDIR)/$(DPATH)/share/pimshit
	cp -r src/* $(DESTDIR)/$(DPATH)/share/pimshit
	install -d $(DESTDIR)/etc/
	install pimshit.conf $(DESTDIR)/etc/

install: install-common
	ln -s $(DESTDIR)/$(DPATH)/share/pimshit/pimshit $(DESTDIR)/$(DPATH)/bin/pimshit

config: pre-config install-common post-config

pre-config:
	$(eval DESTDIR ="/home/$(USER)/.pimshit/")

post-config:
	install -d ~/.bin
	ln -s $(DESTDIR)/$(DPATH)/share/pimshit/pimshit ~/.bin/pimshit
