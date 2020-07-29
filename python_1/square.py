#print a square of user input

square_height = int(input("How high is the square?"))
square_wide = int(input("How wide is the square?"))

a = 1
b = 1

while b <= square_height:
    if b == 1 or b == square_height:
        while a <= square_wide:
            print("*", end='')
            a += 1
    else :
        a = 2
        print("*", end='')
        while a <= square_wide - 1:
            print(" ", end='')
            a += 1
        print("*", end='')
    print()
    a = 1
    b +=1
    