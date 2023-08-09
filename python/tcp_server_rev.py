import socketserver
import subprocess

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    connected = False

    def handle(self):
        # self.request is the TCP socket connected to the client
        
        while True:
            # Prompt user
            self.request.sendall("\n$: ".encode())


            # receive client data
            self.data = self.request.recv(1024).strip()
            user_input = self.data.decode()
            print("{} wrote: {}".format(self.client_address[0], user_input))
           
            
            # quit if asked to do so
            if not user_input or user_input == 'exit': 
                print("Bye!")
                self.request.sendall("Goodbye!".encode())
                exit(0)

            try:

                cmd = user_input.replace("-","+-")
                cmd = [item.strip() for item in cmd.split("+")]
                result = subprocess.run(cmd,stdout=subprocess.PIPE)
                self.request.sendall(result.stdout)

            except Exception as e:
                print(f"Failed : {e}")
                # self.request.sendall(e.encode())


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5500

    # Create the server, binding to localhost on port 5500
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()