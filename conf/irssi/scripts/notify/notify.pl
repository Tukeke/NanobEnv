# Based on Irssi-libnotify by Luke Macken, Paul W. Frields and the idea from 
#
#
#

use Irssi 20020300;
use 5.6.0;
use Socket;
use POSIX;

use vars qw($VERSION %IRSSI %HELP);
$HELP{anotify} = "Have a look at http://xayon.net/";
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
     my ($server, $sumary, $message, $sender) = @_;
     $message =~ s/&/&amp;/g;
     $message =~ s/</&lt;/g;
     $message =~ s/>/&gt;/g;
     $message =~ s/'/&apos;/g;
     $message =~ s/\`/&apos;/g;

                print STDERR "\033[5i";
                print STDERR "TYPE ALERT\n";
                print STDERR "SENDER " . $sender . "\n";
                print STDERR "CONTENT " . $message . "\n";
                print STDERR "\033[4i";
            }
    my %all={};

sub print_text_notify {
    my ($dest, $text, $stripped) = @_;
    my $server = $dest->{server};
    return if (!$server || !($dest->{level} & MSGLEVEL_HILIGHT));
    my $sender = $stripped;
    my $a=Irssi::active_win();
    print CLIENTCRACP $a{'name'};

    $sender =~ s/^\<.([^\>]+)\>.+/\1/ ;
    $stripped =~ s/^\<.[^\>]+\>.// ;
    if ($all{$stripped} == ""){$all{$stripped}=time();}
    else{
    for my $key ( keys %all ) {
        my $value = $all{$key};
    }
            if ($all{$stripped} < time() + 600){ 
                return;
            } else { 
                delete $all{$stripped};
            }
        }
    my $summary = "Hilight in " . $dest->{target};
   
    send_notify($server, $summary, $stripped , $sender);
}

sub message_private_notify {
    my ($server, $msg, $nick, $address) = @_;
    return if (!$server);
 
    if (not $all[$stripped]){$all[$stripped]=time();}
    else{
            if ($all[$stripped] - time() > -10 ){ 
                return;
            } else { 
                $all[$stripped] = time(); 
                #$server->command("whois $sender");
            }
        }

    send_notify($msg, $server, "", $nick);
}

sub dcc_request_notify {
    my ($dcc, $sendaddr) = @_;
    my $server = $dcc->{server};

    return if (!$dcc);
    send_notify($server, "DCC ".$dcc->{type}." request", $dcc->{nick}, $dcc->{nick});
}

Irssi::signal_add('print text', 'print_text_notify');
Irssi::signal_add('message private', 'message_private_notify');
Irssi::signal_add('dcc request', 'dcc_request_notify');

Irssi::command_bind("anotify", "send_notify");
