#Arthmatic Operator
num1 =3
num2 =2
print(f"sum of {num1}and {num2} is {num1+num2}")
print(f"difference of {num1}and {num2} is {num1-num2}")
print(f"product of {num1}and {num2} is {num1*num2}")
print(f"Division of {num1}and {num2} is {num1/num2}")
print(f"Modulus of {num1}and {num2} is {num1%num2}")

print(num1//num2)
print(num1**num2) # 3^2

#Compound Assignment operators
num = 10 
num = num + 5#without compound assignment

num = 10
num+=5 
print(num)#with compound assignment operator
num*=5
print(num)


count =1 
#Increment count
count +=1
print(count)


count=10
#Decrement count
count-=1
print(count)


#Comparison operators

a =10
b =20
c =40
d =30

print(a==b)
print(a>b)
print(a>=b)

#Logical Operators
result_and = a > b and c < d #True and False-> False
print(result_and)

result_and = a > b and C > d #True and True ->True
print(result_and)

result_or = a > b or c < d #True and False -> True
print(result_and)

result_or = a > b #True
print(not result_or)#false

#membership operators

# String is a sequence data type 
data = "python is language"
is_z_present = "z" in data
print(is_z_present)
 
is_z_present ="p" in data
print(is_z_present)

is_z_present="python"in data
print(is_z_present)

#Identity operators
a = 10
b = 20
print(a==b)#Compresion of value
print(a is b)#Comparsion of Memory


#Bitwise Operators







