# Int data type
data = 10
print(type(data))

# Float data type
data = 19.9
print(type(data))

# Complex data type
data = 3 + 5j
print(type(data))

# String data type
data = "String"
print(type(data))

# Boolean data type
data = False
print(type(data))

# List (homogeneous data)
data = [10, 20, 30, 40, 55, 66]
print(type(data))

# Tuple (heterogeneous data)
data = (10, "rahul", True)
print(type(data))

# Set
data = {40, 30, 20, 34, 56}
print(type(data))

# Dictionary
data = {"name": "rahul", "id": 13, "location": "Bangalore"}
print(type(data))

# None type
x = None
print(type(x))


# --------------------------------------
# User defined data type (Class Example)
# --------------------------------------
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def show_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")


# Create an object (instance) of Student class
student_john = Student("John", 101, 89)
student_john.show_details()

# Print the type of object
print(type(student_john))


# --------------------------------------
# Type Conversion done by python automatically
# --------------------------------------
a = 10        # int
print(type(a))

b = 3.5       # float
print(type(b))

c = a + b     # int + float = float
print(c)
print(type(c))


#Type casting (convert by developer forcefully one data tyoe to another data type)
pi = 3.3
print(type(pi))
print(pi)
#Requried round of pi and given whole number
pi_round_int = int(pi)
print(type(pi_round_int))
print(pi_round_int)

rating ="4"
print(type(rating))
#Increment_rating = rating+1 TypeError :can only concatenate String (not"int)to string
Increment_rating = int(rating)
print(Increment_rating)
print(type(Increment_rating))