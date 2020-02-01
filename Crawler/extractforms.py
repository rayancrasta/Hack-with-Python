#! /usr/bin/env python

import requests,re,urlparse
from BeautifulSoup import BeautifulSoup 

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        