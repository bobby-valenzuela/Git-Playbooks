#!/usr/bin/perl -w

use strict;
use Socket;
use Data::Dumper;

# Use public IP unless otherwise specified
my $server = $ARGV[0] || "127.0.0.1";  # Host IP running the server

# use port 7890 as default
my $port = $ARGV[1] || 5500;
my $proto = getprotobyname('tcp');
my $max_conn = 5;

# create a socket, make it reusable
socket(SOCKET, PF_INET, SOCK_STREAM, $proto) or die "Can't open socket $!\n";
setsockopt(SOCKET, SOL_SOCKET, SO_REUSEADDR, 1) or die "Can't set socket option to SO_REUSEADDR $!\n";

# bind to a port, then listen
bind( SOCKET, pack_sockaddr_in($port, inet_aton($server))) or die "Can't bind to port $port! \n";

listen(SOCKET, $max_conn) or die "listen: $!";
print "SERVER started on port $port - awaiting connections...\n";

# accepting a connection
my $client_addr;
my $connected = 0;
my $response;

while ($client_addr = accept(NEW_SOCKET, SOCKET)) {

    my $flags = 0;

    # send them a message, close connection
    my $name = gethostbyaddr($client_addr, AF_INET );
    print "Connection recieved!\n";

    # Write to clients (2 ways)
    send(NEW_SOCKET,"Welcome client!\nEnter a command: ",$flags) if $connected == 0;
    # print NEW_SOCKET "Welcome client!\n" if $connected == 0;
    # $client_socket->send($data);

    # Read from client
    my $buffer = "";
    my $length = 1024;

    while(!$buffer){
        
        # Receive data
        recv(NEW_SOCKET,$buffer,$length,$flags);
        $buffer =~ s/\n//g;
        print "Buffer: [$buffer]\n";

        # Quit if asked
        if($buffer eq 'exit'){
            send(NEW_SOCKET,"Goodbye!\n",$flags);
            close NEW_SOCKET;
            exit(0);
        }
        
        # Exceute cmd
        my $stdout = `$buffer`;
        send(NEW_SOCKET,"$stdout\n",$flags);
        $buffer = "";    
    }

    close NEW_SOCKET;

}
