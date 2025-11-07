#Indentation
#Indentation refers to spaces at the beginning of line
    

#normal Indentation (for normal statment no need to indentation)
print("hello")
# print("morning")#IndentationError: unexpected indent

#conditional with indentation
if 5>2:
#print("yes thats true")#IndentationError: expected an indented block after 'if' statement on line 8
    print("yes thats true")
 #print("incorrect indentation")#unindent does not match any outer indentation level

if True:
    print("this is good")
    print("this is not good")
    print("this is also good")

print("this is also good")

#Condition statment

#If Statment : runs block of code ,if the condition is true
#If (condition):
#    Statments
num = -10
if (num>0):
    print("Number is Positive")

#check if given number is in range of 10 to 20
number =13
if (number >= 10 and number <=20):
    print("Number is in range")

# Check if number is postaive or negative
if (num >0):
    print("Number is positive")
else:
    print("Number is negative")

#Typical voting app
age = 20
if age >=18:
    print("you can vote")
else:
    print("you can not vote")

#Conversion
data = 3.45
print(data)

int_converted_data = int(data)
print(int_converted_data)

#Input(): used to take input from keyword
name = input("Enter your name:")
print("welcome:"+name)

age = input ("Enter your age:")
age=int(age)
if age >= 18:#TypeError: '>=' not supported between instances of 'str' and 'int'
    print("you can vote")
else:
    print("you can not vote")

number = int(input("enter your number:"))
print(number+2)

#above using ternary operators
# variables = value_if_true if condition else value_if_false
age = int(input("Enter your age:"))
status = "you can vote"if age >=18 else "you cannot vote"
print(status)


#elif ladder
marks = int(input("Enter your marks:"))
if marks >=90:
    print("A")
elif marks >=80:
    print("B")
elif marks >=60:
    print("C")
elif marks >=35:
    print("D")
else:
    print("failed")

#match choice
choice = int(input("enter your choice:"))
match choice:
    case 1:
        print("python")
    case 2:
        print("java")
    case 3:
        print("c#")
    case _:
        print("select bt (1-3)")