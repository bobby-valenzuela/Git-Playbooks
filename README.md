# TCP/UDP Server

## UDP Connections

Simple UDP server written in C, Node, Python, and Perl.

<br>

### Start server

<br>

_C_
```bash
gcc c/udp_server.c -o udp_server
./udp_server 5500
```

<br>

_Node js_
```bash
node node/udp_server.mjs
```

<br>

_Python_
```bash
python3 python/udp_server.py
```

<br>

_Perl_
```bash
perl perl/udp_server.pl
```

<br>

_Type 'exit' to stop server listening._

<br>

### Make UDP connection
```sh
nc -u 127.0.0.1 5500
```
^ Replace ip as needed to point to wherever your UDP server is listening.

<br>

Once you've entered that command the prompt will initiate a carriage return where you can enter your datagram message and submit with the "Enter" key.

<br>

Example:
```sh
nc -u 127.0.0.1 5500
Hello World!
```

<br>

## TCP Connections

Simple UDP server written in C, Node, Python, and Perl that allows for reverse shell access.

<br>


## UDP Reverse Shell Connections

<br>

### Start server


<br>

_Node js_
```bash
node node/udp_server_rev.mjs
```

<br>

_Python_
```bash
python3 python/udp_server_rev.py
```

<br>

_Perl_
```bash
perl perl/udp_server_rev.pl
```

<br>

_Type 'exit' to stop server listening._

<br>

### Make UDP connection
```sh
nc -u 127.0.0.1 5500
```
^ Replace ip as needed to point to wherever your UDP server is listening.

<br>

Once you've entered that command the prompt will initiate a carriage return where you can enter your datagram message and submit with the "Enter" key.

<br>

Example:
```sh
nc -u 127.0.0.1 5500
ls -l
```

<br>
