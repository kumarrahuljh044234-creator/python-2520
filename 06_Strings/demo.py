#String

s1 = 'rahul'
print(s1)

s2 = "rahul kumar"
print(s2)

s3 = '''rahul k yadav'''
print(s3)

s4 = """rky"""
print(s4)

#above are for single line strings

#below are multi line Strings

#address = "shastri nagar
#zip is 814101               #Here i defined all the data in double quotes but for multi-line strings
#city is dumka"              i need triple quotes (""" """ or ''' ''')

address = """shastri nagar
zip is 814101               
city is dumka"""

print(address)

#Caution

question = "how are you"
#answer = 'i'm good"
answer = "i'm good"
print(answer)

question = "how are you"
#answer = "i"m good"
answer = 'i"m good'
print(answer)

print("------------------------")

# string
text ="python"

#access whole string
print(text)

#print(text[index])
print(text[0])
print(text[3])
print(text[-2])

#length of string
print(len(text))


    #     0 1  2  3  4  5 (Positive Indexing) (forward)
    #     p  y  t  h  o  n
    #    -6 -5 -4 -3 -2 -1 (Negative Indexing) (backward)

# slicing - slice[start: stop: step]
text = "python"
# print(text[]) # SyntaxError: invalid syntax
print(text[:]) # python
print(text[::]) # python
print(text[0:3]) # pyt 
print(text[1:3]) # yt
print(text[1:3:1]) # yt
print(text[0:5:2]) # pto

    #     0  1  2  3  4  5 (Positive Indexing) (forward)
    #     p  y  t  h  o  n
    #    -6 -5 -4 -3 -2 -1 (Negative Indexing) (backward)

print(text[-4:-1]) # tho
print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty
print(text[1:4:-1]) # empty
print(text[-1:-4:]) # empty


# slicing 
print(text[::-1]) # nohtyp

text = "python"
reversed_text = ""

# custom login
for char in text:
    reversed_text = char + reversed_text # ...typ
print(reversed_text)


text = "python"
# print(text[index]) 
print(text[0]) 
print(text[3]) 
# print(text[10]) # IndexError: string index out of range

print(text[0:6:-1])

#Concatenation means joining two or more strings together.
#String concatenate
a = "hi"
b = "rahul"
print(a+b)

a = 10
b = 20
print(a+b)

#String formating
age = 26
#print("my age is: "+age)#TypeError: can only concatenate str (not "int") to str

#Interpolation  (String Interpolation means inserting values (variables) inside a string.)
print(f"my age is:{age}")
print("my age is:",age)
print("my age is:", +age)
print("my age is: "+str(age))

print("my age after 5 year would be:",+age+5)


#String repetition (String repetition means repeating a string multiple times using the * operator.)
laugh = "haha"
print(laugh)

laugh_toomuch = "hahahahahahahahahahahahahahahahahahahahahahahahahahahaha"
print(laugh_toomuch)

laugh_toomuch = laugh*30
print(laugh_toomuch)

#String immutability (Immutability = Cannot be changed after creation)
greet = "hello"
print(greet)

print("i am trying to change the value in existing value")
#greet[0] = "H"
#print(greet)

