import { info } from 'console';
import dgram from 'dgram'
import { exit } from 'process';

const port = 5500;
const host = "127.0.0.1";
const socket = dgram.createSocket("udp4");

// Listen for incoming connnections. (best to always specify an ip otherwise will default to listen on all ips)
socket.bind(port, host, () => { 
    console.log(`Listening...\n`)
});

// Handling Connections
socket.on("message", (msg, info) => {
    // Can print buffer as-is - but changing to strin to we have access to JS methods (need to remove newlines)
    msg = msg.toString('utf8');
    console.log(msg);

    console.log(`Someone Connected!\nDatagram received: ${msg.replace('\n','')}<-`);
    console.log(`
        === Datagram Info ===
        Addr: ${info.address}
        Port: ${info.port}
        Size: ${info.size}
        IP Type: ${info.family}
    `);

    socket.send("hi",info.port)

    if (msg == "exit") { 
        console.log("Exiting!");
        exit(0);
    }

});