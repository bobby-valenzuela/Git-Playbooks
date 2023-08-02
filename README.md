# TCP/UDP Server

## UDP Connections

### UDP Server (Node js)
```bash
node udp_server.mjs
```

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