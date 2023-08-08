#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

void main(int argc, char **argv){

    // Define port
    if(argc != 2){
        printf("Usage: %s <port>\n", argv[0]);
        exit(0);
    }

    int port = atoi(argv[1]);
    // Socket file descriptor
    int sockfd;                 
    
    // Structs for addresses
    struct sockaddr_in myAddr, remoteAddr;
    
    // Receive data from datagrams (1024 bytes)
    int buffSize = 1024;
    char buffer[buffSize];

    // Address Size has struct
    socklen_t addr_size;

    // Create ipv4 socket (AF_INET) using udp (SOCK_DGRAM)
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    // Configure my address struct
    memset(&myAddr, '\0', sizeof(myAddr));
    myAddr.sin_family = AF_INET;
    myAddr.sin_port = htons(port);
    myAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Begin listening: Bind socket we made to our address
    bind(sockfd, (struct sockaddr*)&myAddr, sizeof(myAddr));
    addr_size = sizeof(remoteAddr);

    char end_str[] = "exit";

    // Keep printing while we're receiving something
    while(recvfrom(sockfd, buffer, buffSize, 0, (struct sockaddr*)& remoteAddr, &addr_size)){

        int i = 0;
        int strSize = 0;

        // get string size
        for (i = 0; i < buffSize; i++){
            if(buffer[i] == '\n') break;
            if(buffer[i] == '\r') break;
            if(buffer[i] == '\0') break;
            strSize++;
        }

        // Build found string
        char found_str[strSize];

        for (i = 0; i < strSize; i++) found_str[i] = buffer[i];
        found_str[strSize] = '\0';

        printf("[+] Data Received: %s\n", found_str);

        // If they typed "exit" then stop listening on server
        if(strcmp(end_str,found_str) == 0){
            
            printf("[-] Exiting Program!\n");
            exit(0);

        }

    }

}