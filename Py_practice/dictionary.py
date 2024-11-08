dic = { }
n=int(input("How many number you want to add in directory:"))
for i in range(n) :
    name = input( "Enter name of friend :-")
    phone = int( input("Enter phone number of friend :-" ))
    dic [name] = phone
    

print()
print(dic)

#input any name and print phone number of that particular name
print()
print("a :-")
name = input( "Enter name of that friend which you want to search his phone number :-")
if name in dic :
    print(phone)

#Add New contact:
print()
print("b :-")
name = input( "Enter name of friend :-")
phone = int(input("Enter phone number of friend :-" ))
dic [name] = phone
print(dic)

#Delete a contact
print()
print("c :-")
name = input( "Enter name of that friend which you want to delete :-")
del dic[ name ]
print(dic)

#Updata an existing phone number
print()
print("d :-")
name = input( "Enter name of that friend which you want to change his phone number :-")
phone = int(input ("Enter phone number of friend :-" ))
del dic [ name]
dic[ name ] = phone
print(dic)


print()
print("e :-")
newdic = {}
key = list( dic.keys())
key.sort()
for i in key :
    newdic [ i ] = dic [ i ]
print(newdic)
