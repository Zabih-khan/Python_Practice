
x = "Hello world ! How are you."
print(x)
#---------------string-------------------

str = "Hello world"
print(str[0])

for i in str:
    print(i ,end = " ")

#---------------string-------------------
print()
str1 = "includehelp"
print(str1[0])
print("~~~~~~~~~~~~~~~~~~")
print("Origianal-->",str1)
print()
print("str1[2:5]-->",str1[2:5])
print("str1[1:6]-->",str1[1:6])
print("str1[0:4]-->",str1[0:4])
print("str1[:]-->",str1[:])
print("str1[:0]-->",str1[:0])
print("str1[:1]-->",str1[:1])
print("str1[:3]-->",str1[:3])
print("str1[1:]-->",str1[1:])
print("str1[5:]-->",str1[5:])
print("~~~~~~~~~~~~~~~~~~")
print("4 element tak jawo aur pehla two element ko ignore karo aur bake element ko print karo")
print("str1[2:4]-->",str1[2:4])
print("~~~~~~~~~~~~~~~~~~")
print("Mulitply-->",str1 * 2)

print("***********************************************")

print("""
Appending text at the end of the string using += operator
""")
str = "Zabih"
#concatinate of one more string
str += "allah"
print("stirng concatination:-->",str)

print("***********************************************")
print("""
QUESTION:Cancatenate two string and assign in another string by using + operator
""")
str11 = "Hello"
str22 = "world"
str3 = str11 + "" + str22
print(str11)
print(str22)
print("Concatenated string:-->",str3)

print("***********************************************")
print("""
QUESTION:check if a substring present in a string using "in" operator.
""")
str = "IncludeHelp.com"
substr = "Help"
if substr in str:
    print("yes . substring present in the string;")
else:
    print("No . substring no present in the string;")

print("***********************************************")
print("""
QUESTION:Assign Hexadecimal value in the string and print it in the string format.
""")
str = "\x41\x42\x43\x44"
print(str)

print("***********************************************")
print("""
 QUESTION:How to print double quotes with the string varaible
""")

string = "Hello world"
print('"%s"' % string)
print('"{}"'.format(string))

print("***********************************************")
print("""
python program to convert a list of the characters into a string.
""")

list = ['a','b','c','d','e']
print("list:-->",list)
print("convert into a string")
str = ""
for i in list:
    str += i
print(str)
print("Type:")
print( type(str))














































































































