def number_game():
    user_input = int(input("Guess Number between 5 and 50: "))
    magic_number = 6   
    if user_input == magic_number:
        print("ARE YOU A MIND READER")
    elif user_input > 50:
        print("You're too high.")
        number_game()
    elif user_input < 5:
        print("You're too low.")
        number_game()
    else:
        print("Sorry try again.")
        number_game()

number_game()
