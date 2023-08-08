#!/usr/bin/env python3

import socket
import subprocess

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

    # Parse args
    cmd = message.replace("-","+-")
    cmd = [item.strip() for item in cmd.split("+")]
    result = subprocess.run(cmd,stdout=subprocess.PIPE)
    # result_decode = result.stdout.decode('utf-8') <- actually no need to decode because would have to re-encode to send back as a reply  
    server_socket.sendto(result.stdout, address)
    