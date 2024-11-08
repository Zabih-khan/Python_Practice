
n = 10
print("Enter {} values:".format(n), end="")
lst = []
for _ in range(n):
    lst.append(abs(int(input())))
def avg(lst_):
    return sum(lst_) / len(lst_)

def prime(lst_):
    primes = []
    for num in lst_:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    return primes

def even(lst_):
    return len([i for i in lst_ if i % 2 == 0])

print(avg(lst))
print(prime(lst))
print(even(lst))
