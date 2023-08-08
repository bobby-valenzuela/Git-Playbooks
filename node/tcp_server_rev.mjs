import net from 'net';
import { exec } from 'child_process';

const server = net.createServer(socket => {

    // Upon client connection
    console.log(`TCP Handshake successful with ${socket.remoteAddress}:${socket.remotePort} [Type: ${socket.remoteFamily}]`)

    // Respond to client
    socket.write("Hello client! I hear you loud and clear!\n");
    
    // Upon Receiving data from client
    socket.on("data", data => {
       
        const cmd = data.toString();
        
        exec(cmd, (err, stdout, stderr) => {
            if (err) {
                // node couldn't execute the command
                return;
            }
            else {
                // socket.send(stdout, info.port)
                socket.write(stdout);
            }
        });


    });

});

console.log("Listening...")
server.listen(5500, '127.0.0.1');