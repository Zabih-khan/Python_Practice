# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
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

    
