import { info } from 'console';
import dgram from 'dgram'

const port = 5500;
const host = "127.0.0.1";
const socket = dgram.createSocket("udp4");

// Listen for incoming connnections. (best to always specify an ip otherwise will default to listen on all ips)
socket.bind(port, host, () => { 
    console.log(`Listening...\n`)
});

// Handling Connections
socket.on("message", (msg, info) => {

    console.log(`Someone Connected!\nDatagram received: ${msg}`);
    console.log(`
        === Datagram Info ===
        Addr: ${info.address}
        Port: ${info.port}
        Size: ${info.size}
        IP Type: ${info.family}
    `);

});