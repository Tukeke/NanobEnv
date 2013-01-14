DPATH="/usr/"
all: install

install:
	install -d $(DESTDIR)/$(DPATH)/share/pimshit
	cp -r src/* $(DESTDIR)/$(DPATH)/share/pimshit
	install pimshit.conf /etc/
	ln -s $(DESTDIR)/$(DPATH)/share/pimshit/pimshit $(DESTDIR)/$(DPATH)/bin/pimshit
