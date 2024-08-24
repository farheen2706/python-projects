import hashlib #python library for hashing

print("**************PASSWORD CRACKER ******************")#display line

pass_found = 0 

input_hash = input("Enter the hashed password:")#getting the hashed password as input and storing it in the variable
pass_doc = input("\nEnter passwords filename including path(root / home/):")#stores the path of he passwords file name

try:
 pass_file = open(pass_doc, 'r')
 
except:

 print("Error:")
 
 print(pass_doc, "is not found.\nPlease give the path of file correctly.")
 quit()#closes the program in case of errors for error handling

for word in pass_file:#reads all the values in the file
 #print(word)
 enc_word = word.encode('utf-8')#converting to encoded
 hash_word = hashlib.md5(enc_word.strip())#hashing the value in this function
 digest = hash_word.hexdigest()#converts into hexadecimal string
 #print(digest)
 if digest == input_hash:#compares the values from the file and finds the password
     print("Password found.\nThe password is:", word)
 pass_found = 1

