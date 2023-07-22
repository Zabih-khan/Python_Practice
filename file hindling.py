text_file = open("write_it.txt", "w")
print("Please write that you want to write in your file\n")

s=input()
text_file.write(s)

text_file.close()
