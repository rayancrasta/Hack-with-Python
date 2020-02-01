#! /usr/bin/env python

import requests,urlparse
from BeautifulSoup import BeautifulSoup 

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url= "http://10.0.2.15/multidae/index.php"
response  = request(target_url)

parsed_html = BeautifulSoup(response.content)
formsList= parsed_html.findAll("form")

for form in formsList:
    action=form.get("action")
    post_url=url_parse.urljoin(target_url,action)
    #print(post_url)
    method=form.get("method")
    #print(method)

    inputs_lits= form.findAll("input")
    post_data= {}

    for inputname in inputs_lits:
        inputname= input.get("name")
        #print(inputname)
        input_type= input.get("type")
        input_value=input.get("value")
        if input_type=="text":
            input_value = "test"
        post_data[inputname]= input_value
    requests.post(post_url,data=post_data)
