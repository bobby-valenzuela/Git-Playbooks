import net from 'net';

const server = net.createServer(socket => {

    // Upon client connection
    console.log(`TCP Handshake successful with ${socket.remoteAddress}:${socket.remotePort} [Type: ${socket.remoteFamily}]`)

    // Respond to client
    socket.write("Hello client! I hear you loud and clear!\n");

    // Upon Receiving data from client
    socket.on("data", data => {
       
        console.log(`Received Data: ${data.toString()}`);

    });

});

console.log("Listening...")
server.listen(5500, '127.0.0.1');