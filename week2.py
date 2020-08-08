#! /usr/bin/env python3

import os
import requests

path ='/data/feedback/'
keys=['title','name','date','feedback']

folder=os.listdir(path)
for file in folder:
  keycount = 0
  f={}
  with open(path+file) as file:
    for line in file:
      value=line.strip()
      f[keys[keycount]]=value
      keycount=keycount+1
    print(f)
    response=requests.post("http://<External IP Address>/feedback/",json=f)
print(response.request.body)
print(response.status_code)

