## Put me in ~/.irssi/scripts, and then execute the following in irssi:
##
##       /load perl
##       /script load notify
##

use strict;
use Irssi;
use vars qw($VERSION %IRSSI);

$VERSION = "0.01";
%IRSSI = (
    authors     => 'Jared Quinn',
    origauthors => 'Luke Macken, Paul W. Frields, ',
    contact     => 'jared@jaredquinn.info',
    name        => 'notify.pl',
    description => 'Use libnotify to alert user to hilighted messages',
    license     => 'GNU General Public License',
    url         => 'http://jaredquinn.info/irssi',
);

Irssi::settings_add_str('notify', 'notify_icon', 'gtk-dialog-info');
Irssi::settings_add_str('notify', 'notify_time', '5000');
Irssi::settings_add_str('notify', 'notify_command', 'remote-notify-send');

sub notify {
    my ($server, $summary, $message, $sender) = @_;
    # Make the message entity-safe
    $message =~ s/&/&amp;/g; # That could have been done better.
    $message =~ s/</&lt;/g;
    $message =~ s/>/&gt;/g;
    $message =~ s/'/&apos;/g;

                print STDERR "\033[5i";
                print STDERR "TYPE IRC\n";
                print STDERR "ICON " . Irssi::settings_get_str('notify_icon') . "\n";
                print STDERR "SHOWFOR " . Irssi::settings_get_str('notify_time') . "\n";
                print STDERR "SUBJECT " . $summary . "\n";
                print STDERR "SENDER " . $sender . "\n";
                print STDERR "CONTENT " . $message . "\n";
                print STDERR "\033[4i";
}

sub print_text_notify {
    my ($dest, $text, $stripped) = @_;
    my $server = $dest->{server};
    return if (!$server || !($dest->{level} & MSGLEVEL_HILIGHT));
    my $sender = $stripped;
    $sender =~ s/^\<.([^\>]+)\>.+/\1/ ;
    $stripped =~ s/^\<.[^\>]+\>.// ;
    my $summary = "Hilight in " . $dest->{target};
    notify($server, $summary, $stripped , $sender);
}

sub message_private_notify {
    my ($server, $msg, $nick, $address) = @_;
    return if (!$server);
    notify($server, "Private message from ".$nick, $msg, $nick);
}

sub dcc_request_notify {
    my ($dcc, $sendaddr) = @_;
    my $server = $dcc->{server};

    return if (!$dcc);
    notify($server, "DCC ".$dcc->{type}." request", $dcc->{nick}, $dcc->{nick});
}

Irssi::signal_add('print text', 'print_text_notify');
Irssi::signal_add('message private', 'message_private_notify');
Irssi::signal_add('dcc request', 'dcc_request_notify');
