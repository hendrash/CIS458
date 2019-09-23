import hashlib


def crackHash(hash):
    filepath = 'combin' 
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            result=hashlib.md5(line.rstrip("\n\r").encode()).hexdigest()
            if result == hash:
                print("hash cracked !!!")
                print("the hash "+ result +" is equal to "+line)
                return
            print(result+" "+hash)
    
    print("failed to crack the hash make sure your hash or word is 3 or less plain text characters")

def collision(hash):
    hashVal=hash
    hashVal=hashlib.md5(hashVal.encode()).hexdigest()
    while hash[:3] != hashVal[:3]:
        hashVal=hashlib.md5(hashVal.encode()).hexdigest()
        print(hash+" "+ hashVal) 
    print("found a collision from the first three hash bits "+hash[:3])

#main
print("This is a brute force cracker that can crack 3 character words")
print("[0] enter a 3 character string to be cracked")
print("[1] enter a hash to find the string")
print("[2] enter a string to find the hashes collision")
print("[3] enter a hash to find a collision\n")
option = input("> ")
if option == 0:
    str = raw_input("enter in a 3 character word all lower case\n")
    result = hashlib.md5(str.encode()).hexdigest();
    print("Your calculated hash is "+result);
    print("Now attempting to crack this hash though brute force. This next part might take a few minutes ....")
    crackHash(result)   

elif option == 1:
    print("enter a hash of a string of 3 characters or less")
    hashVal=raw_input("enter in your hash\n")
    crackHash(hashVal)

elif option == 2:
    str = raw_input("enter in a string for a collection comparing only the first 3 characters in the hash\n")
    result= hashlib.md5(str.encode()).hexdigest();
    print("Your calcuated hash is "+result)
    print("Now attempting to find a collision ")
    collision(result)
else:
   str=raw_input("enter a hash of a string") 
   result=hashlib.md5(str.encode()).hexdigest();
   crackHash(str)




