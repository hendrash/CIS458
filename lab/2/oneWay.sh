#! /bin/bash

function crackHash(){
input="combin"
while IFS= read -r line
do
  sol="$( printf "%s" "$line" | md5sum - | cut -d ' ' -f 1 )" 	
	if [ $sol == $1 ]
	then 
	echo hash cracked !!!
	echo the hash  $sol is equal to $line
		exit
	fi
	echo $sol $1
done < "$input"
echo failed to crack hash make sure your hash or word is 3 or less characters long and a-z lowercase 
}

#main
echo This is a one-way resistant hash function 
echo [0] enter a 3 character string to be cracked
echo [1] enter a hash from a 3 character string to be cracked
read  choice
echo $choice

if [ $choice = 0 ]
then
	echo enter in a 3 character word all lower case
	read string
	h="$(printf "%s" "$string" | md5sum - | cut -d ' ' -f 1)"
	echo Now attempting to crack through brute force. This next part might take a minute .....
	crackHash $h 
else
	echo enter in your hash
	read hashVal
	crackHash $hashVal
fi





