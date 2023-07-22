a=[]
def enqueue(val):
    a.append(val)
    print("Item successfully inserted:")
def dequeue(a):
    x=a.pop(0)
    print("item is successfully dequeue")
def peak(a):
    x=a[0]
    print("paek element",x)
    
def display(a):
    print("We have the following item in list:")
    for i in range(len(a)):
        print(a[i])
if __name__=="__main__":
    ch=()
    while(True):
        print("""
    1-enqueue
    2-dequeue
    3-peak
    4-display
    5-Exit

""")
        ch=int(input("ENTER:"))
        if ch==1:
            val=int(input("Enter the value:"))
            enqueue(val)
        elif ch==2:
            if len(a)==0:
                print("queue is empty:")
            else:
                dequeue(a)
        elif ch==3:
            if len(a)==0:
                print("queue is empty:")
            else:
                peak(a)
        elif ch==4:
            display(a)
        elif ch==5:
            break
        else:
            print("Enter wrong number !please select valid option:")
            
        
