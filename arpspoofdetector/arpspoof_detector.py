#!/usr/bin/env python
import scapy.all as scapy

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

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)
    #stor=flase states that dont save the packets to avoid loss

            
def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op ==2 : #check arp resonses
        try:
            real_mac= get_mac(packet[scapy.ARP].psrc)
            response_mac= packet[scapy.ARP].hwsrc
            
            if real_mac != response_mac:
                print("[+] Youre under attack")
        except IndexError:
            pass

sniff("wlp3s0")