number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

int_num = int(number1)                  # whole number becomes an int (instead of string)
float_num = float(number2)              # the string gets casted as a float (one decimal place)
round_num = int(round(float_num))       # the decimal is rounded to the nearest whole number
                                        # and then cast as an int (loses the .0)
print(int_num, float_num, round_num)