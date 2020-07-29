#print a square of user input

square_size = int(input("How large is the square?"))

a = 1
b = 1

while b <= square_size:
    while a <= square_size:
        print("*", end='')
        a += 1
    print()
    a = 1
    b +=1



