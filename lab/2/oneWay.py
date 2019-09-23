import hashlib


def crackHash(hash):
    filepath = 'combin' 
    trials=0 
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            trials+=1
            result=hashlib.md5(line.rstrip("\n\r").encode()).hexdigest()
            if result == hash:
                print("hash cracked !!!")
                print("the hash "+ result +" is equal to "+line)
                print("the process took "+str(trials)+" trials")
                return
            print(result+" "+hash)
    
    print("failed to crack the hash make sure your hash or word is 3 or less plain text characters")

def collision(hash):
    hashVal=hash
    hashVal=hashlib.md5(hashVal.encode()).hexdigest()
    trials=0
    while hash[:3] != hashVal[:3]:
        trials+=1
        hashVal=hashlib.md5(hashVal.encode()).hexdigest()
        print(hash+" "+ hashVal) 
    print("each hash output is a hash of the previous hash value")
    print("found a collision from the first 24 bits "+hash[:3])
    print("the process took "+str(trials)+" trials")

#main
print("This is a brute force cracker that can crack 3 character words")
print("[0] enter a 3 character stringing to be cracked")
print("[1] enter a hash to find the stringing")
print("[2] enter a string to find the hashes collision")
print("[3] enter a hash to find a collision\n")
option = input("> ")
if option == 0:
    string = raw_input("enter in a 3 character word all lower case\n")
    result = hashlib.md5(string.encode()).hexdigest();
    print("Your calculated hash is "+result);
    print("Now attempting to crack this hash though brute force. This next part might take a few minutes ....")
    crackHash(result)   

elif option == 1:
    print("enter a hash of a stringing of 3 characters or less")
    hashVal=raw_input("enter in your hash\n")
    crackHash(hashVal)

elif option == 2:
    string = raw_input("enter in a stringing for a collection comparing only the first 3 characters in the hash\n")
    result= hashlib.md5(string.encode()).hexdigest();
    print("Your calcuated hash is "+result)
    print("Now attempting to find a collision ")
    collision(result)
else:
   string=raw_input("enter a hash of a stringing") 
   result=hashlib.md5(string.encode()).hexdigest();
   crackHash(string)




