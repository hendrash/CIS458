#!/bin/bash

# hashfunction  hashvalue the message and the password 

key=$(sed -n '2p' .authenticate) 
openssl dgst -md5 -hmac $key $1 >> .authenticate


thereHash=$( sed -n '1p' .authenticate | cut -d' ' -f2 ) 
yourHash=$(sed -n '3p' .authenticate  | cut -d' ' -f2) 


echo comparing the following two hashes 
echo $thereHash
echo $yourHash

sed -i '3d' .authenticate

if [ $thereHash == $yourHash ]; then
	echo files are the same
else
	echo files are different
fi

