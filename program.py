alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
def encrypt(plaintxt,key):  
  ciphertxt=""
  for char in plaintxt: 
    position=alphabet.index(char)
    newpos=(position+key)%26: 
    ciphertxt+=alphabet[newpos]
    print("the text after encryption is: (ciphertxt)")
def decrypt(ciphertxt,key): 
  plaintxt=""
  for char in ciphertxt:
   position=alphabet.index(char)
    newpos=(position-key)%26: 
    plaintxt+=alphabet[newpos]
    print("the text after decry is:  position=alphabet.index(char)
    newpos=(position+key): 
    ciphertxt+=alphabet[newpos]
    print("the text after decryption is: (plaintxt)")  
endCode=False
while not endCode:
  username=input("Type encrypt for encryption and decrypt for decryption: ")
  txt=input("type the message")
  
  
