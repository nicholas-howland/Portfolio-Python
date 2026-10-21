from scapy.all import *
from time import sleep
import argparse
from random import randint
from threading import Event

def main():

## argument parsing
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-t','--target', required=True, type=str, help="Target IP address")
    parser.add_argument('-r','--protocol', choices = ["tcp","udp"],required=True, type=str, help="Protocol to use only tcp and icmp are supported currently")
    parser.add_argument('-p','--port', required=True, type=int, help="Port to scan")
    parser.add_argument('-c','--count', required=False, default=3, type=int, help="Number of packets to send")
    parser.add_argument('-f','--flags', choices = ["SA","S"],required=False, default="S", type=str, help="Flags to send on a TCP scan")
    parser.add_argument('-i','--interface', required=False, type=str, help="Interface to use for scanning")
    parser.add_argument('-v','--verbose',required=False,action=argparse.BooleanOptionalAction,default=False,type=bool, help="Be verbose and output all IPID's in the packet not just the summary")
    args = parser.parse_args()

## start an async sniffer so we can see what happened durring the scan0
    if(args.interface=="UNSET"):
        t = AsyncSniffer(filter="(tcp or icmp) and ((dst "+args.target+") or (src "+args.target+"))")
    else:
        t = AsyncSniffer(filter="(tcp or icmp) and ((dst "+args.target+") or (src "+args.target+"))",iface=args.interface)
    t.start()

## put a happy little sleep here so the sniffer can start
    sleep(1)

    if(args.protocol=="tcp"):
        for i in range(args.count):
            p = IP(dst=args.target)/ TCP( dport=int(args.port) , sport = randint(49152,65535), flags=args.flags )        
            send(p,verbose=False)
    if(args.protocol=="udp"):
        for i in range(args.count):
            p = IP(dst=args.target)/ UDP( dport=int(args.port) , sport = randint(49152,65535))        
            send(p,verbose=False)

    ## put a slightly longer sleep but just as happy sleep here so we get returns from the packets sent
    time.sleep(3)

    ## Stop the sniffer
    pc = t.stop()
    results = []
    sessions = pc.sessions()
## prints out all packets sent
    print("IP Address:Port  TCP Flags")
    for k,v in sessions.items():
# print out specifics about the packets from our target
        for i in sessions[k]:
#            print(i)
            if(args.protocol=="tcp"):
                if(args.target == i["IP"].src and args.port == i["TCP"].sport):
                    if(args.verbose):
                        print(str(i["IP"].src)+":"+str(i["IP"].sport)+" "+str(i["TCP"].flags))
                    elif( str(i["IP"].src)+":"+str(i["IP"].sport)+" "+str(i["TCP"].flags) not in results ):
                        results.append(str(i["IP"].src)+":"+str(i["IP"].sport)+" "+str(i["TCP"].flags))
            if(args.protocol=="udp"):
                if(args.target == i["IP"].src and args.port == i["TCP"].sport):
                    if(args.verbose):
                        print(str(i["IP"].src)+":"+str(i["IP"].sport)+str(i["UDP"].show()))
                    elif( str(i["IP"].src)+":"+str(i["IP"].sport)+" "+str(i["UDP"].flags) not in results ):
                        results.append(str(i["IP"].src)+":"+str(i["IP"].sport)+" "+str(i["UDP"].flags))


    for i in results:
        print(i)

if __name__ == "__main__":
    main()
