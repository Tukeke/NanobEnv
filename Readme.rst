Copim, personal information management for the not-so-common users
--------------------------------------------------------------------

Copim is a set of tools and configurations designed to ease the
integration between mutt, wyrd, abook and irssi.

Features
----------

- Standard mutt with sidebar configuration, with an example of
      how can multiple imap accounts be managed
- Wyrd is a TUI for reminder, wich we've integrated with a
      graphical reminder advice via libnotify (GUIs are bad, but neccesary sometimes)
- Abook is a TUI contact adress, we've integrated it in the mutt config, and added 
      a wrapper via goobook to import google contact's settings (see
      ~/.copim/goobook/sample for a sample conffile)
- Irssi comes out with a bunch of preinstalled plugins, like the ones about notifications.
      Have a look at notification section later.

Dependecies
------------------

- libnet-twitter-perl
- wyrd 
- goobook
- mutt-patched
- abook 
- irssi 
- screen or tmux (for tmux you'd have to hack it! I'll upload a tmux config soon tough)

Installation
--------------

If you want to have support for google contacts you should install my fork of goobook from http://gitorious.org/~xayon/goobook/xayon-abook
After having all deps installed, you should run (as root) 

::

    make install
    
After that, just execute copim.

Side notes
--------------

Not that, in copim, everything is saved under the ~/copim directory, except irssi logs, that will require you to either disable the autolog facility (wich is in most cases the usual thing, but not for me ;-) ) or create /var/log/irssi/username and giving it the user permissions, this could be done with this commands:

::

    mkdir -p /var/log/irssi/USERNAME && chown -R USERNAME:USERNAME /var/log/irssi/USERNAME

As everything gets saved there, making a backup is reasonably easy.

Notifications
-----------------

Notifications are enabled by default when you're not away, and they'll generate
a ssh connection to the host where you've conencted from (this is dangerous!).
Make sure you've exchanged keys with that host and is accesible via ssh from the 
outside, and that you've confirmed host vereification (try it by sshing the host
yourself), after that, just install libnotify-bin in the remote host (the client,
I meant ;) ) and you'll be free to go. 

Mobile notifications.
-----------------------

You can also edit your config file, register in notifo.com, and add your key 
and username there.
After that you'll just need to configure anotifo client in your phone, and you'll
have notifications enabled there.

