
#!/usr/bin/env python3
import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    #created instance of the parser object

    parser.add_argument("-i","--interface",dest='interface',help="Interface to change the mac address")

    parser.add_argument("-m","--mac",dest='newmac',help="newmac address")

    ops= parser.parse_args()

    if not ops.interface:
            parser.error(" please specify a interface")
    elif not ops.newmac:
        parser.error("Please specify a mac")
    return ops

#function for changing mac address
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def getcurentmac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig',interface])
    #use rgeular expression to get only the max from the output
    mac_address_search=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("couldnt get macc adress")

    
#call the functions
ops = get_arguments()
#ops conatins values like interfaec and newmac

interface= ops.interface
newmac = ops.newmac

oldmac =getcurentmac(interface)
print("Old mac is >"+str(oldmac))

#now change the mac
change_mac(interface,newmac)

newmac= getcurentmac(interface)
print("New mac is  > "+str(newmac))

