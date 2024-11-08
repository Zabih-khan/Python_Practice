inche = 0.0254
foot = inche * 12
yard = foot * 3
mile = yard * 1760

meter=int(input("Enter meter:"))

meter=float(meter)

inche=meter/inche
foot=meter/foot
yard=meter/yard
mile=meter/mile

print("{m:g} metres is equivalent to {i:g} inches:".format(m=meter,i=inche))
print("{m:g} metres is equivalent to {f:g} foot:".format(m=meter,f=foot))
print("{m:g} metres is equivalent to {y:g} yard:".format(m=meter,y=yard))
print("{m:g} metres is equivalent to {x:g} mile:".format(m=meter,x=mile))

