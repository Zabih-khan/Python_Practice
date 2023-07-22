dict={}
while(True):
    
    print("========Birthday App========")
    print("1.show Birthday")
    print("2.Add to birthday List")
    print("3.Exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        
        if len(dict.keys())==0:
            
            print("Nothing to show :")
        else:
            name=input("Enter Freind's Name")
            birthday=dict.get(name,"No data found")
            print(birthday)
    elif choice==2:
        name=input("Enter Friend's Name")
        date=input("Enter Birthday")
        dict[name]=date
        print("Birthday Added")
    elif choice==3:
        
        break
    else:
        print("Choose a valid option")
