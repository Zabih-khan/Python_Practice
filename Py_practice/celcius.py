
while(True):
    ch=int(input("1-Fahrenhai to celsius:\n2-Celsius to Fahrenhait:\nSelect option:"))
    print()
    if ch==1:
        f=int(input("Enter Temperature:"))
        cel=(f - 32.0) * 5.0/9.0
        print("Temperautre in celsius:",cel,"°C")
        print()
    if ch==2:
        c=int(input("Enter Temperature:"))
        fah=(c * 9.0/5.0) + 32.0
        print("Temperature in fahrenhait:",fah,"°F")
        print()
