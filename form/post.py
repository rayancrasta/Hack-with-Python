#!/usr/bin/env/python

#how to fill froms using python
import requests

target_url="http://10.0.2.5/dvwa/login.php"

data_d = {"username":"admin","password":"password","Login":"submit"}

response = requests.post(target_url,data=data_d)

print(response.content)