def sum_list(lst):
    if len (lst)==1:
        return lst[0]
    else:
        return lst[0]+sum_list(lst[1:])

print(sum_list([2,3,4,5,6]))



