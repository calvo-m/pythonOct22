number1 = float(input("Enter first number: "))          # eg 3
number2 = float(input("Enter second number: "))         # eg 6

if number1 > number2:       # this is not the case in the example                
    number1bigger = True
else:                       # this is the case, therefore it becomes false                                               
    number1bigger = False

print("It is ", number1bigger, " that number 1 is bigger.")