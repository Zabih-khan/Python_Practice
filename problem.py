n=10
print("Enter {} values:".format(n))
lst=[]
for i in range(n):
    lst.append(int(input(">>")))
print(lst)

def average(list):
    x=sum(list)
    ave= x/2
    print('Average:',ave)


#count prime number:
def prime(lst_):
     primes = []
     for num in lst_:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                
                primes.append(num)

     print(primes)

average(lst)
prime(lst)
