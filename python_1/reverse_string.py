a_string = "This is a string"
a= len(a_string) - 1
b_string = ""
while  a >= 0:
    b_string = b_string + a_string[a]
    a -= 1

print(b_string)
