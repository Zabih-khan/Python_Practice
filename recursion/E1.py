def to_string(n,base):
   conver_tString = "zabihullah"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,10))
