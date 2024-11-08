a=[]
def enqueue(val):
    a.append(val)
    print()
    
    print("ELEMENT SUCCESSFULLY INSERTED:")
def dequeue():
    x=a.pop(0)
    print()
    print("ELEMENT SUCCESSFULLY DELETED:")
def peak(a):
    print()
    print ("PEAK ELEMENT",a[0])
def display(a):
    print()
    print("WE HAVE THE FOLLOWING ELEMENT IN THE QUEUE:")
    for i in range (len(a)):
        print("* ",a[i])
        print()
if __name__== "__main__":
    while(True):
        ch=int(input("1->ENQUEUE\n2->DEQUEUE\n3->PEAK\n4->DISPLAY\n5->EXIT\nSELECT OPTION:"))
        if ch==1:
             val=int(input("ENTER THE VALUE :"))
             enqueue(val)
        elif ch==2:
            if len (a)==0:
                print("QUEUE IS EMPTY:")
            else:
                dequeue(a)  
        elif ch==3:
            if len (a)==0:
                print("QUEUE IS EMPTY:")
            else:
                peak(a)
        elif ch==4:
            if len (a)==0:
                print("QUEUE IS EMPTY:")
            else:
                display(a)

        elif ch==5:
            print()
            print("==>GOOD BYE <==")
            break
        



                

        
