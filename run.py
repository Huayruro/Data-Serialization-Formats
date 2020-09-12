#!/usr/bin/env python3
import os
import requests
# Uploads all the feedback stored in this folder to the company's website
dire="/data/feedback"
# company's website feedback url
url = 'http://35.184.134.27/feedback/'

# keys for the content value
headers=["title", "name", "date", "feedback"]
# returns a list of all files and directories in the specified path
files = os.listdir(dire)

for file in files:

  try:
    with open(os.path.join(dire,file), mode='r',encoding='UTF-8') as feed:
      #initialize counter for headers and dictionary 
      i=0
      diccio={}
      for line in feed.readlines():
        diccio[headers[i]]=line
        i+=1
      # post the dictionary to the company's website.
      x = requests.post(url=url, data = diccio)
      #check if posting was succesfull
      if x.status_code==201:
        print("Success posting ",file)
      else:
        print("Error posting ",file)
  except :
        print("Error reading", file)
