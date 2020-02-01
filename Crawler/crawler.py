#! /usr/bin/env python

import requests

#finding subdomains

def requestss(url):
    try:
        return requests.get('http://'+url)
    except Exception:
        pass

target_url="stea1th.tech"

with open("/root/Desktop/Pyth/Crawler/Subdomain.txt","r") as wordlists:
    for line in wordlists:
        word=line.strip()
        test_url=word+"."+target_url
        response= requestss(test_url)
        if response:
            print("[+] Discovered subdomain -->"+test_url)
        

