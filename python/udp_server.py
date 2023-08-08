#!/usr/bin/env python3

import socket

host = '127.0.0.1'
port = 5500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print("Listening...\n\n")

while True:
    message_bytes, address = server_socket.recvfrom(1024)
    
    # Decode + Remove newlines
    message = message_bytes.decode()
    message = message.replace("\n", "")
    message = message.replace("\r", "")

    print(f"Client: {message}")

    # Handle exit msg
    if message == "exit":
        response = "Exiting!".encode()
        server_socket.sendto(response, address)
        exit(0)