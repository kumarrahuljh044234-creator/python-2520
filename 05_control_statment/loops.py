#loops:repetitive action
counter =1
while counter <=5:
        print(counter)
        counter = counter+1

#while when you don't know number of Iteration in adavance
atm_pin = 4234 #actual pin
user_input =0

while user_input != atm_pin:
    user_input = int(input("enter PIN:"))

print("you can withdraw")

#For loop
#Used to iterate over a sequence

data = 10 #int :not a sequence
print(id(data))#memory add
print(type(data))#data type
print(dir(data))#Attributes supported

# for character in data :#TypeError:'int'object is not iterable
# print(Character)

data = "ten"#str :sequence of characters
print(type(data))
print(dir(data))

for character in data:
    print(character)

    #How to know iterable object -dir (object)

    list_number = [10,20,30,40,50]
    print(dir(list_number))
     for number in list_number
        print(number)