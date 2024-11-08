n=int(input("How many student do you want to store in list:"))
student=[]
grade=[]
for i in range (n):
    name=input("Enter the name:")
    marks=float(input("Enter marks:"))
    student.append([name,marks])
    grade.append(marks)#this is for calculation of 2nd lowest marks

print()
print("\nThis is a list of student and its marks:",student)

print("\nThis is a grade of students:",grade)
grade=sorted(set(grade))#sorted unique
print("\nAfter sorting the grade of student:",grade)
m=grade[1]
print("\nNow 2nd lowest grade is:",m)
name=[]
count=0
for val in student:
    if m==val[1]:
        name.append(val[0])
print("\nThis is a name of student who's 2nd lowest grade :",name)

name.sort()
print("\nAfter sorted student name ",name)


for nm in name:
    count+=1
    print(nm)
print("Thers is",count,"student who take 2nd lowest grade")

    
