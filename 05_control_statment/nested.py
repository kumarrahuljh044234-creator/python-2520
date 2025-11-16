#Nested condition

age = int(input("Enter your age: "))
has_id = input("do you have an Id(yes/no)?: ")

if age >=18:
    if has_id =="yes":
        print("you can vote")
    else:
        print("you need an id to vote")
else:
    print("you are to young to vote")

#Nested loops

for row in range(1, 8):           # Outer loop (1 to 5)    #range(start, stop, step)

    for column in range(1, 4):       # Inner loop (1 to 5)
        print(f"{row} * {column} = {row*column}")
    print("-------------------")     # Blank line after each table

#Outer loop (row) → decides which table (1 to 5).
#Inner loop (column) → goes through numbers (1 to 5).
#Nested loops together → produce all combinations of multiplication.
#Blank line (print()) → separates each table for clarity.


#While with Nested 
 
#while(condition):
#statment

row =1 
while row <6:
    column =1
    while column<6:
        print(f"{row}*{column}={row*column}")
        column+=1
    print("_______________")
    row+=1