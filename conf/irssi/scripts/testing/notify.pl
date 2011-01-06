use Irssi 20020300;
use 5.6.0;
use Socket;
use POSIX;

use vars qw($VERSION %IRSSI %HELP);
$HELP{sms} = "
";
$VERSION = "0.0b";
%IRSSI = (
        authors         => "David Francos (XayOn)",
        contact         => "xayon\@xayon.net",
        name            => "notify",
        description     => "/anotify",
        license         => "GNU GPLv2 or later",
        changed         => "Thu Ago 12 03:54:07 CET 2010"
);

sub send_notify {
     my ($message, $server, $witem) = @_;
     $message =~ s/&/&amp;/g;
     $message =~ s/</&lt;/g;
     $message =~ s/>/&gt;/g;
     $message =~ s/'/&apos;/g;

                print STDERR "\033[5i";
                print STDERR "TYPE ALERT\n";
                print STDERR "SENDER " . $sender . "\n";
                print STDERR "CONTENT " . $message . "\n";
                print STDERR "\033[4i";
            }

Irssi::command_bind("notify_manager", "send_notify");
