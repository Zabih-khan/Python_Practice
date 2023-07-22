def where1(x, y):
    if x > 0: 
        print ('quadrant I or IV')
    if y > 0:
        print ('quadrant I or II')
def where2(x, y):
    if x > 0:
        print ('quadrant I or IV')
    elif y > 0:
        print ('quadrant II')
        
for x, y in (-1, 1), (1, 1):
    
    where1(x,y)
    where2(x,y)
