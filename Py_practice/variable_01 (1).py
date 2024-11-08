def makeInc(x):
    def inc(y):
     # x is "attached" in the definition of inc
        print( y + x)
    print (inc)

incOne = makeInc(1)
incFive = makeInc(5)
incOne(5) # returns 6
incFive(5) # returns 10
