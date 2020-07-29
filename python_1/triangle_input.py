#print a square of user input

tri_height = int(input("How high is the triangle?"))
#square_wide = int(input("How wide is the square?"))



def space_func (num_spaces):
    c = 1
    while c <= num_spaces:
        print(" ", end='')
        c += 1

def ask_func (num_asks):
    a = 1
    while a <= num_asks:
        print("*", end='')
        a += 1

total_ask = (tri_height * 2) - 1
start_space = (total_ask - 1)/2
start_ask = 1
b = 0

while b < tri_height:
    space_func(start_space - b)
    ask_func((start_ask + (b * 2)))
    space_func(start_space - b)
    print()
    b += 1

    