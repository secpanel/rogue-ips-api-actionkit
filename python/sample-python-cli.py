#!/usr/bin/env python
 
#Importing modules for HTTPS Connection
import urllib
import httplib
 
#Importing modules for parsing JSON
import json

#Importing modules for reading Command Line Arguments
import sys

LIMIT=10 # default limit
OFFSET=0 # default offset


#Function to print the Usage, in case invalid arguments
def usage():
   print "python ",sys.argv[0]," <api-key> [limit] [offset]"
   print "or, if file is executable"
   print sys.argv[0]," <api-key> [limit] [offset]"
   #Abort any further processing
   sys.exit(1)

#Function to make a HTTPS call and resturn the response,
#from Secpanel's Rogue IP service provider server 
def getTheData(key,limit,offset):
   h = httplib.HTTPSConnection('apis.secpanel.com');
   h.request('GET', '/rouge-ips-json.php?key='+str(key)
                                +'&limit='+str(limit)+'&offest='+str(offset))
   response = h.getresponse()
   return response.read()

#Validating command line arguments
if len(sys.argv) < 2:
  #No key provided
  usage()
elif len(sys.argv) == 2:
  #Seems api-key is supplied
  KEY=sys.argv[1]
elif len(sys.argv) == 3:
  #Seems api-key as well as limit are supplied
  KEY=sys.argv[1]
  LIMIT=sys.argv[2]
elif len(sys.argv)== 4:
  #Seems key,limit and offset value are also supplied
  KEY=sys.argv[1]
  LIMIT=sys.argv[2]
  OFFSET=sys.argv[3]
else:
  #More than required arguments supplied
  usage()
 
#Get the JSON Data
json_response=getTheData(KEY,LIMIT,OFFSET)

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
