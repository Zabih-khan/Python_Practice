def convert(n,base):
    convert_string='asdfg'
    if n<base:
        return convert_string[n]
    else:
        return convert(n//base,base)+convert_string[n%base]
print(convert(11,5))
