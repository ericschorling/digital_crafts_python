user_string = input("Give me a string")
histo_dict = {}

for x in user_string:
    histo_dict[x] = 0
for x in user_string:
    histo_dict[x] += 1

print(histo_dict)