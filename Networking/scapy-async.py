#!/usr/bin/python3

from scapy.all import *
import argparse
from os import system

def main():
## parser script
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', type=str, help="Target IP address")
    parser.add_argument('-c','--count', type=int, help="Number of packets to send")
    parser.add_argument('-o','--output', type=str, help="Pcap output file")
    parser.add_argument('-p','--protocol', type=str, help="Protocol to use")
    args = parser.parse_args()

    print()

    args = parser.parse_args()


## Async sniffer packet capture    
    t = AsyncSniffer(filter="tcp")
    t.start()
# do stuff
    system("curl example.com")
    time.sleep(1)
#    time.sleep(1)
    pc = t.stop()
## write the packets to a capture file
    wrpcap("test.pcap",pc)    
## list values from the pcap
    p = rdpcap("test.pcap")
    s = rdpcap("test.pcap");
    sessions = s.sessions()
## will print all of the sessions
#    print(sessions)
#    print(s[0])

## prints out all packets sent    
    for k,v in sessions.items():
        print(k)
# print out specifics about the packets
        print(sessions[k][0].id)
    
    # get a set of packets based on netflow data
#    s['NETFLOW data'][0].id



if __name__ == "__main__":
    main()
