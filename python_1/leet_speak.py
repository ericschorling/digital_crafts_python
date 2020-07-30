user_string = input("Give me a string: ")
leet_string = ""
x=0

while x < len(user_string):
    if user_string[x] == "a" or user_string[x] == "A":
        leet_string = leet_string + ("4")
        x += 1
    else :
        leet_string += user_string[x]
        x += 1
print(leet_string)