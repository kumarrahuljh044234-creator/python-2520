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


#Redirecct call based on isd code
mobile_num = input("Enter your mobile number with isd code: ")
if mobile_num.startswith("+91"):
    print("calling india")
elif mobile_num.startswith("+1"):
    print("calling USA")
elif mobile_num.startswith("+86"):
    print("calling china")
else:
    print("calling support avilable only to india , china & usa")


#Email synchronization -> gmail.com.
source_email = input("Enter your email ID: ")
destination_email = ("Enter your email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("synchronization")
else:
    print("synchronization failed both providers should of same type")


#gmail remove spaces at the beginning and ending od email id provided..
email = input ("Enter your email ID: ")
format_email = email.strip()
print(format_email)


# csv / excel lot of data in rows .
# Name,City,Age,Email,Role
emp_row = "John,Hyd,25,john@gmai.com,Developer"
print("Original Data: "+emp_row)
# ['John,Hyd,25,john@gmai.com,Developer']
fields = emp_row.split(",")
# ['John', 'Hyd', '25', 'john@gmai.com', 'Developer']
print(fields)

# print emp name and role
print("Name: "+fields[0])
print("Role: "+fields[4])