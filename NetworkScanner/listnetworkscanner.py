#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp packet object \\ 
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #setting the broadcast mac
    #print(arp_request.summary())
    arp_request_broadcast=broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)
    
    print("IP\t\t\tMAC adress\n------------------------------------------------")
    for element in answered:
        print(element[1].psrc+"\t\t"+element[1].hwsrc)
        #the psrc and hwsrc fields can be seen in element[1].show
        #psrc and hwsrc are the Ip and Arp of the client
        print("-------------------------------------")

scan("192.168.1.0/24")
