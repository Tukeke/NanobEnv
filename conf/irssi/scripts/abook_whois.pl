#!/usr/bin/perl
use Symbol;
use vars qw($VERSION %IRSSI); 
$VERSION = "0.1";
%IRSSI = (
    name	=> "Irssi copim, integrates irssi with copim, looking for nickname fields in abook .",
    description	=> "Show IRC userinfo extracted from a abook-like file in ~/.abook/",
    license	=> "Public Domain",
);

Irssi::theme_register(['whois_userinfo', '{whois userinfo $1}']);my $mynick;
sub get_current_nick_data { return `copim.abook @_ `;}
sub get_current_nick_mobile { return `copim.abook @_|cut -d, -f2|cut -d" " -f2 &`; }
sub call{ $fone=get_current_nick_mobile($_[0]); chomp($fone); $server->command("anotify Call:+34$fone");return;}
sub dcall{ $server->command("anotify Call:$_[0]");return;}
sub stop_call{ system("copim.call Stop");return;}
sub mail{ $mail=`copim.abook $_[0]|cut -d- -f1 &`; system("screen -X at Mail stuff 'm' && screen -X at Mail stuff '$mail'");}
sub make_call{ $fone=&get_current_nick_mobile($_[0]); chomp($fone); print CLIENTCRAP "Calling $fone for $_[0]";  return &call($fone); }
sub event_whois { my ($server, $data) = @_; my ($temp, $nick) = split(" ", $data); $mynick=$nick; }
sub event_end_of_whois {my ($server) = @_; if ($mynick) { $server->printformat($nick, MSGLEVEL_CRAP, 'whois_userinfo',$nick, &get_current_nick_data($mynick)); $mynick = undef; }}


Irssi::command_bind("remote_call", "make_call");
Irssi::command_bind("dcall", "dcall");
Irssi::command_bind("mail", "mail");
Irssi::command_bind("stop_call", "stop_call");

Irssi::signal_add_first('event 311', 'event_whois');
Irssi::signal_add_first('event 318', 'event_end_of_whois');
