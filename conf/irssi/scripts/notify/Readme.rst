About irssi passtrought notification plugin
===========================================

A while ago I read about passtrough notification for irssi with passtrough printing, I really loved the concept, except for I found a few bugs on it:
    - Flooding: It could be annoying one person sending you the same message once and once again
    - Not filtering strings being passed to the shell script: You could execute malicious code because of this.
    - Not easy to install / launch / configure.

It's an amazingly ingenious system, perfect for many-ssh-sessions-connected one-only-server configurations, and to not need more than one ssh connection for notifications.

Installing
==========

    Just put notifier script on the path you want, install the script on irssi/scripts or irssi/scripts/autorun and configure it according to configuring section.


Configuring
=============

Make sure to have in all your clients' xresources file (normally .Xresource or .Xdefaults on debian) the following lines

::

    *XTerm*printerAutoClose: true
    *XTerm*printerCommand: /usr/bin/notifier
 
Replace /usr/bin/notifier for the path where you put the notifier. The notifier must be in the client's side, as this conf file, not in the server.

FAQ
====

Q: What if my irssi is in the same computer where I want my notifications to be?
A: Why the hell are you using this system then?

