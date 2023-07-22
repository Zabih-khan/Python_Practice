# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands. 
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT

#=====================================================================




#Here we also use function for appending,removeing or insertig etc:
#you can see i create a fuction but i comment it .it work Totaly




##def insertintolist(l,x,y):
##    l.insert(x,y)

if __name__=="__main__":
    n=int(input("Enter the number:"))
    l=[]
    for i in range(n):
        inp=input("Enter:")
        
        if inp.find("insert")>=0:
            a=inp[7:]
            x,y=a.split()
            x=int(x)
            y=int(y)
            l.insert(x,y)
##          insertintolist(l,x,y)

        elif inp.find("remove")>=0:
            b=inp[7:]
            b=int(b)
            l.remove(b)

        elif inp.find("append")>=0:
            c=inp[7:]

            c=int(c)
            l.append(c)

        elif inp.find("sort")>=0:
            
            l.sort()

        elif inp.find("pop")>=0:
            l.pop(-1)

        elif inp.find("print")>=0:
            print(l)
            
        elif inp.find("reverse")>=0:
            l.reverse()
            










            

            
        
        
