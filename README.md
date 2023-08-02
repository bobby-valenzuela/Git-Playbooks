# TCP/UDP Server

## UDP Connections

<br>

### Start server

<br>

_Node js_
```bash
node udp_server.mjs
```

<br>

_C_
```bash
gcc udp_server.c -o udp_server
./udp_server 5500
```
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

## UDP Connections

