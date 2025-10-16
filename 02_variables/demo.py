#Working with variables
student_name = "Rahul"
student_age = "27"
student_cgpa = 8.1
student_passed = True


#Reterive the data
print(student_name)
print(student_age)
print(student_cgpa)
print(student_passed)

#get Identity /Memory Address
print(id(student_name))
print(id(student_age))
print(id(student_cgpa))
print(id(student_passed))

# Get data type
print(type(student_name))
print(type(student_age))
print(type(student_cgpa))
print(type(student_passed))

#In python a variable can change during the execution

dynamic_data = 10
print(type(dynamic_data))
dynamic_data = "10"
print(type(dynamic_data))
dynamic_data =10.0
print(type(dynamic_data))
dynamic_data = True
print(type(dynamic_data))

#python memory model

a = 10
print(id(a))
b = 20
print(id(b))
c = 10
print(id(c))
# a,b,c int values which is simple data type(one only value)

#python has complex data type (more than one Value)

list_nums_a = [10,20,30,40,50] # List is created using [values1,values2,values3.....values-n]
print(type(list_nums_a))
print(id(list_nums_a))

list_nums_b = [10,20,30,40,50]
print(type(list_nums_b))
print(id(list_nums_b))

#To accesss data inside list we use index ->index start from 0 1 2....
#0,1,2,3,4,
#[10,20,30,40,50]
print(list_nums_a)
print(list_nums_b)

print(list_nums_a[0])
print(list_nums_b[1])

print(id(a))
print(id(c))
print(id(list_nums_a[0]))
print(id(list_nums_b[0]))


#observation to be made
x="python"
y="is"
z="easy"
#print(xyz) NameError: name 'xyz'is not defines

#python is easy
print(x+y+Z) #Concatenation

x=10
y=20
z=30
print(x+y+z) #Addition operator

#name and age
name = "Rahul"
age = 27
print("my name is"+name"and my age is"+age)# typeError :can only concatenation string To string (not "int")