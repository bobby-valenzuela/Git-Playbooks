import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        
        while True:

            # receive client data
            self.data = self.request.recv(1024).strip()
            print("{} wrote: {}".format(self.client_address[0], self.data.decode()))
            
            # quit if asked to do so
            if not self.data.decode(): 
                print("Bye!")
                self.request.sendall("Goodbye!")
                exit(0)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5500

    # Create the server, binding to localhost on port 5500
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()