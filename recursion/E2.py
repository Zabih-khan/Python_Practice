def recursive_list(data_list):
    total=0
    for element in data_list:
        if type(element)==type([]):
            total=total+recursive_list(element)
        else:
            total=total+element
    return total

print(recursive_list([2,3,[4,6],[6,8,9]]))
