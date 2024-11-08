x=str(input("want yo quit"))
while(x!="quit"):
    a=int(input("plz enter your money"))
    b=str(input("plz enter your currancy"))
    dollar=a*150
    darham=a*29
    pound=a*138
    if (b=="dollar"):
          print("plz enter currancy",dollar)
    elif(b=="darham"):
          print("plz enter currancy",darham)
    elif(b=="pound"):
          print("plz enter currancy",pound)
    else:
           print("wrong currancy")
           x=str(input("want to quit"))
