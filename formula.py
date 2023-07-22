def formula(m,v0,t,a):

##    m=1/3(*v0*s)
##    v0 = 3 *m/s
##    t = 1 *s
##    a = 2 *m/s**2
    s = v0*t + 0.5*a*t**2
    print ("The answer is :",s)

formula(int(input("Enter the value of m:")),
int(input("Enter the value of v0:")),
        int(input("Enter the value of t:")),
        int(input("Enter the value of a:"))

        )
