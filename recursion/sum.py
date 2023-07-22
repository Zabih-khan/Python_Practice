def sum_list(n):
    if len(n)==1:
        return n[0]
    else:
        return n[0] + sum_list(n[1:])
print(sum_list([2,3,4,5,6]))
