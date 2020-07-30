list_to_check = [1,2,2,3,4,4,1,2,3,4]
new_list = []
x = 0
y = 0
new_list.append(list_to_check[0])

for x in list_to_check:
    for y in new_list:
        if x == y:
            break
        elif (y == new_list[-1]):
            new_list.append(list_to_check[x])
            break
        else:
            continue


print(new_list)