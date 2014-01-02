NanobEnv
=========
Nanobes might probably be the smallest living organism on earth.

NanobEnv is a completly-text-based environment, with all the things you probably
need to make a full computing user experience. Thus making nanobenv the smallest
environment for a linux desktop.

.. image:: https://raw.github.com/XayOn/NanobEnv/master/nanobenv.png


Installing
===========

NanobEnv can be installed without root privileges (and this is the default).
Just

::

make install

And start it with nanobEnv tmux for the default profile.

Profiles
++++++++++
The "pim" profile launches by default this applications:
messaging calendar mail contacts

The "common" profile launches this ones instead:
files music torrent

Deps
+++++

NanobEnv requires a few applications to run correctly, have a look at
nanovenv.conf to see the required "drivers".

Right now, for a complete experience, recommended apps are the following:
    weechat
    calcurse
    mutt
    abook
    goobook
    mc
    deluge
    cmus

NanobEnv makes extensive use of tmux, remember to install it.

::

    apt-get install tmux weechat calcurse mutt abook goobook mc deluge cmus


NanobEnv requires (sort of) prettier terminal
(http://github.com/XayOn/prettierTerminal) and cursedXDG
(http://github.com/XayOn/cursedXDG).

Components
============

Personal information manager
+++++++++++++++++++++++++++++++

The PIM part of NanobEnv has:

    - Google Calendar integration
    - Google Contacts integration
    - Gmail integration
    - Nice wizards for first configs
    - Solarized colors for almost everything
    - Integration with bitlbee
      - (planned): calls with gtalksms
      - (planned): See your contacts information from google contacts
    - (planned): ToDo list sync with google calendar

Common
++++++++

The common component contains:
    - Torrent
    - File browser
    - Music player
