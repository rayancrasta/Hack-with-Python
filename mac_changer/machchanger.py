#!/usr/bin/env python

import subprocess

interface=input("enter the interface")
newmac=input("enter the new mac")

subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+newmac+",shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)

print("Changed the mac for "+interface+" to"+newmac)