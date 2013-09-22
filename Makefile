DPATH="/usr/"
all: install

install-common:
	install -d $(DESTDIR)/$(DPATH)/share/nanobenv
	cp -r src/* $(DESTDIR)/$(DPATH)/share/nanobenv
	install -d $(DESTDIR)/etc/
	install nanobenv.conf $(DESTDIR)/etc/

install: install-common
	ln -s $(DESTDIR)/$(DPATH)/share/nanobenv/nanobenv $(DESTDIR)/$(DPATH)/bin/nanobenv

config: pre-config install-common post-config

pre-config:
	$(eval DESTDIR ="/home/$(USER)/.nanobenv/")

post-config:
	install -d ~/.bin
	ln -s $(DESTDIR)/$(DPATH)/share/nanobenv/nanobenv ~/.bin/nanobenv
