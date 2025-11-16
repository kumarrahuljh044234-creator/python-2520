#String methods

#Simulate gmail user id input formatting
email = input ("Enter your id: ")
format_email = email.lower()+"@gmail.com"  #(@gmail--String concatination),(lower making sure that ever the input i got it was converted all the lower case)
print("Original Input: "+email)
print("formated output: "+format_email)

#simulate PAN 

pan = input("Enter your PAN")

if pan.isalnum():
    format_pan = pan.upper()
    print("user give pan: "+pan)
    print("formatted PAN: "+format_pan)
else:
    print("user given PAN is invalid: "+pan)