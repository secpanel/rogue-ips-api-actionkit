#!/usr/bin/env python
 
#Importing modules for HTTPS Connection
import urllib
import httplib
 
#Importing modules for parsing JSON
import json
 
def getTheData(key,limit=10,offset=0):
   h = httplib.HTTPSConnection('apis.secpanel.com');
   h.request('GET', '/rouge-ips-json.php?key='+str(key)
                                +'&limit='+str(limit)+'&offest='+str(offset))
   response = h.getresponse()
   return response.read()
 
#Get the JSON Data
json_response=getTheData("your-key")

#Parse JSON String
parsed_json = json.loads(json_response)
#Create a blank Dictionary to store ip and respective
#Geolocation attributes
ips={}
 
#Read the parsed JSON
for keys in parsed_json:
    if keys=='limit':
        limit_used=parsed_json[keys]
    elif keys=='offset':
        offset_used=parsed_json[keys]
    elif keys=='total':
        total_records=parsed_json[keys]
    elif keys=='status':
        status=parsed_json[keys]
    elif keys=='status_code':
        status_code=parsed_json[keys]
    else:
        #Store the IPs
        ips[keys]=parsed_json[keys]
 
#Process as per application logic
if status_code==200:
#data is good for and useful
   if total_records < 1:
      print "No records returned"
   else:
      for ip in ips:
         print ip,":",ips[ip],"\n"
else:
   print "Something went bad : [",status_code,"] ",status,"\n"
