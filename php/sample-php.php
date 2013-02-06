<?php
 
function fetchTheData($api_key,$limit=10,$offset=0)
{
   $json_content=file_get_contents("https://apis.secpanel.com/rouge-ips-json.php?key=$api_key&limit=$limit&offset=$offset");  
   return $json_content;
}
 
 
//Receive the APIs response
$json=fetchTheData("your-key");
 
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
