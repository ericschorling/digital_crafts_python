the_string = input("Give me a string: ")

replace_dict = {
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m",
}

a = 0
decoded_string = ""

while a < len(the_string):
    if the_string[a] == " ":
        decoded_string = decoded_string + the_string[a]
        #print("nope")
        a += 1
    else :
        decoded_string = decoded_string + replace_dict[the_string[a]]
        #print("yep")
        a += 1
a += 1
print(decoded_string)