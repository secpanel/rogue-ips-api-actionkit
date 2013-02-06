<?php

$LIMIT=10; // default limit
$OFFSET=0; // default offset

//Function to print the Usage, in case invalid arguments 
function usage(){
  die($argv[0]." <api-key> [limit] [offset]\n");
}

function fetchTheData($api_key,$limit,$offset){
   $json_content=file_get_contents("https://apis.secpanel.com/rouge-ips-json.php?key=$api_key&limit=$limit&offset=$offset");  
   return $json_content;
}

//Validating Command line arguments
if(count($argv)<2){
 //No api-key provided
 usage();
}else if(count($argv)==2){
 //Seems api-key is supplied
 $KEY=$argv[1];
}else if(count($argv)==3){
 //Seems api-key as well as limit are supplied
 $KEY=$argv[1];
 $LIMIT=$argv[2];
}else if(count($argv)==4){
 //Seems api-key,limit and offset value are also supplied
 $KEY=$argv[1];
 $LIMIT=$argv[2];
 $OFFSET=$argv[3];
}else{
 //More than required arguments supplied
 usage();
}
 
//Receive the APIs response
$json=fetchTheData($KEY,$LIMIT,$OFFSET);
 
//Parse the JSON
$parsedJSON=json_decode($json,true);
 
//Create a blank array to Hold all the
//IPs and their Geolocation Attributes
$ips=array();

//Read the parsed JSON
foreach($parsedJSON as $k=>$value){
   switch($k)
   {
       case 'limit':
          $limit_used=$parsedJSON['limit'];
          break;
       case 'offset':
          $offset_used=$parsedJSON['offset'];
          break;
       case 'total':
          $total_records=$parsedJSON['total'];
          break;
       case 'status':
          $status=$parsedJSON['status'];
          break;
       case 'status_code':
          $status_code=$parsedJSON['status_code'];
          break;
      default:
          //Store the IPs
          $ips[$k]=$value;
   }
}

 
//Process as per application logic
if($status_code=='200')
{
    //data is good for and useful
    if($total_records<1)
    {
       echo "No records returned";
    }else{
       foreach($ips as $ip=>$geolocation)
       {
          echo "$ip : ";
          print_r($geolocation);
          echo "\n";
       }
    }
}else{
  echo "Something went bad : [$status_code] $status\n";
}
?>
