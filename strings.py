# input of a user is read as a string
userName = input("Enter here your name: ")
# and can be cast to a different data type (in some occasions)
userNumber = int(input("How many cats do you want?: "))

example1 = "Hello "
example2 = "You want"

# strings can be concatenated with other data types
print(example1 + userName + "\n" + example2, userNumber, "cats")