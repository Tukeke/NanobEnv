# Show IRC userinfo (http://irc-galleria.net, finnish only) information
# on /WHOIS or /userinfo

# version 1.13
# for irssi 0.8.0 by Timo Sirainen
use Symbol;
use vars qw($VERSION %IRSSI); 
$VERSION = "0.1";
%IRSSI = (
    name	=> "Irssi abook, integrates irssi with abook, looking for nickname fields.",
    description	=> "Show IRC userinfo extracted from a abook-like file in ~/.abook/",
    license	=> "Public Domain",
);

Irssi::theme_register(['whois_userinfo', '{whois userinfo $1}']);my $mynick;
sub get_current_nick_data { return `abook_parser all $_[1]`;}
sub event_whois { my ($server, $data) = @_; my ($temp, $nick) = split(" ", $data); $mynick=$nick; }
sub event_end_of_whois {my ($server) = @_; if ($mynick) { $server->printformat($nick, MSGLEVEL_CRAP, 'whois_userinfo',$nick, &get_current_nick_data()); $mynick = undef; }}

Irssi::signal_add_first('event 311', 'event_whois');
Irssi::signal_add_first('event 318', 'event_end_of_whois');
