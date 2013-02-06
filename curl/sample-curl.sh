#!/bin/bash

#Setting the default values for optional arguments
limit=10 # default limit
offset=0 # default offset

#Subroutine to print coreect usage, in case of validiation failure
usage(){
    echo "Usage: $0 api-key [limit] [offset]"
    exit
}

if [ $# -lt 1 ]
 then
    usage 
 elif [ $# -eq 1 ]; then
  #Seems api-key is supplied
  api_key="$1"
 elif [ $# -eq 2 ]; then
  #Seems api-key as well as limit are supplied
  api_key="$1"
  limit="$2"
 elif [ $# -eq 3 ]; then
  #Seems api-key,limit and offset value are also supplied
  api_key="$1"
  limit="$2"
  offset="$3"
 else
  #More than required arguments supplied
  usage
 fi

curl https://apis.secpanel.com/rouge-ips-json.php?key=$api_key\&limit=$limit\&offset=$offset > response.json

cat response.json
