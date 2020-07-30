user_string = input("Give me a string: ")
leet_string = ""
leet_dict = {
    "a" : "4",
    "e" : "3",
    "g" : "6",
    "i" : "1",
    "o" : "0",
    "s" : "5",
    "t" : "7",
}
x=0

while x < len(user_string):
    if user_string[x].lower() in leet_dict:
        leet_string = leet_string + leet_dict[user_string[x].lower()]
        x += 1
    else :
        leet_string += user_string[x]
        x += 1
print(leet_string)