a=[]
def push(a,val):
    a.append(val)
    print("Element successfully pushed:")
def pop(a):
    val=a.pop()
    print("pop item:",val)
def peek(a):
    index=len(a)-1
    print("Peek element:",a[index])
def display(a):
    
    print("We have the following element in the list:")
    for i in range (len(a)-1,-1,-1):
        print(a[i])
if __name__=="__main__":
    while(True):
        ch=int(input("1-push\n2-pop\n3-peek\n4-display\n5-Exit\nEnter the choice:"))
        if ch==1:
            val=int(input("Enter the number:"))
            push(a,val)
        elif ch==2:
            if len (a)==0:
                print("Stack is Empty:")
            else:
                pop(a)

        elif ch==3:
            if len(a)==0:
                print("Stack is empty:")

            else:
                peek(a)

        elif ch==4:
            if len(a)==0:
                print("Stack is empty:")

            else:
                display(a)

        elif ch==5:
            break

        else:
            print("Enter wrong number ! Please select the valid option:")

        print("Press c to continue and q to quit:")

##        choice=()
##        while(choice!="c" and choice!="Q"):
##            choice=input("Enter the choice:")
##
##            if choice=="c":
##                continue
##
##            elif choice=="q":
##                break
##            
##            
##
##        

            
