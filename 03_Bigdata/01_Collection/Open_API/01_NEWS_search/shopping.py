#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
client_id = "23rQCPSxLajmI32f1QGW"
client_secret = "cMYtKVbcGW"
url = "https://openapi.naver.com/v1/datalab/shopping/categories";
body = "{\"startDate\":\"2018-01-01\",\"endDate\":\"2018-12-31\",\"timeUnit\":\"month\",\"category\":[{\"name\":\"베이스메이크업\",\"param\":[\"50000194\"]},{\"name\":\"라면\",\"param\":[\"50001083\"]}],\"device\":\"pc\", \"age\":[\"40\", \"50\"], \"gender\":\"m\"}";



request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)