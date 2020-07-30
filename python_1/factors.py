factor_num = int(input("Give me a number: "))

factor_arr = []
large_fact = factor_num
small_fact = 1

a = 1

while a <= factor_num:
    if factor_num % a == 0 :
        small_fact = a
        large_fact = int(factor_num / a)
        if large_fact < small_fact:
            break
        else:
            factor_arr.append(large_fact)
            factor_arr.append(small_fact)
            a += 1
    else:
        a += 1

factor_arr.sort()
print(factor_arr)