#!/usr/bin/python

import requests, json, sys
from subprocess import call, check_output

import os
Data = str(check_output("xsel"))
Desc = "Code" # sys.argv[2]
Filename = "File1" # sys.argv[3]
url = u"https://api.github.com/gists"
PostData ='{"description":"'+ Desc + '","public":"true","files":{"' + Filename  + '":{"content":"'+ Data +'"}}}'
print PostData
r = requests.post(url=url, data = PostData )
Content = r.json()
html_url = Content["html_url"]
command = "echo " +  html_url + " | xclip -selection clipboard"
call(command, shell=True)
