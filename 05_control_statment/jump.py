#Branching statment(jump statment)
#Break

for number in range(1,20):
    print(number)

    print("_______break___________")

for number in range(1,20):
    if number == 10:
        break
    print(number)

    print("________continue___________")

#continue
#Used to skip the current iteration and move to the next loop iteration.
for number in range(1,20):
    if number ==5:
        continue
    print(number)

print("_____pass____________")

#Pass
#Does nothing — used as a placeholder when no code is needed (to avoid error
emp_salary = 10001
if emp_salary >10000:
    print("high salary")

for i in range(5):
    if i == 3:
        pass 
    print(i)