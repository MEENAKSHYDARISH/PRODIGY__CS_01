alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
def encrypt(plaintxt,key):  
  ciphertxt=""
  for char in plaintxt: 
    position=alphabet.index(char)
    newpos=(position+key)%26 
    ciphertxt+=alphabet[newpos]
  print(f"the text after encryption is: {ciphertxt}")
def decrypt(ciphertxt,key): 
  plaintxt=""
  for char in ciphertxt:
   position=alphabet.index(char)
   newpos=(position-key)%26
   plaintxt+=alphabet[newpos]
  print(f"the text after decryption is:{plaintxt}" )
  
endCode=False
while not endCode:
  username=input("Type encrypt for encryption and decrypt for decryption: ")
  txt=input("type the message: ")
  shift=int(input("enter the shift key:\n"))
  if username=="encrypt":
    encrypt(plaintxt=txt,key=shift)
  elif username=="decrypt":
    decrypt(ciphertxt=txt,key=shift)
  continuecode=input("Type 'yes' if you want to run the code again,'no' if not: ")
  if continuecode=="no":
    enCode=True
    print("THANKYOU!")
    break
  
  
