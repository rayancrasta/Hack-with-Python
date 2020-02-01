#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    #created instance of the parser object

    parser.add_argument("-t","--target",dest='target',help="Target IP adress range to scan")

    ops= parser.parse_args()

    if not ops.target:
            parser.error(" please specify a interface")
    return ops

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp packet object \\ 
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #setting the broadcast mac
    #print(arp_request.summary())
    arp_request_broadcast=broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)
    #srp is used to generate packets
    
    client_list=[]    
    for element in answered:

        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        client_list.append(client_dict)
        #print(element[1].psrc+"\t\t"+element[1].hwsrc)
        #the psrc and hwsrc fields can be seen in element[1].show
        #psrc and hwsrc are the Ip and Arp of the client
        print("-------------------------------------")
    return client_list

def print_result(results_list):
    print("IP\t\t\tMAC adress\n------------------------------------------------")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])

ip_ops = get_arguments()
ip=ip_ops.target
scan_result=scan(ip)
print_result(scan_result)