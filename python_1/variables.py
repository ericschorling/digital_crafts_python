user_name = input("whats your name")
print(user_name)

user_age= int(input("what is your age"))
age_in_ten_years = str(user_age + 10)
print("In 10 years you will be " + age_in_ten_years)

print("%s is a string %d is an integer, %.2f is a float" % ("foo", 10, 3.1420))