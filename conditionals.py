# ask for user input
mark = int(input("Enter your mark here: "))

# check different grade boundaries
if mark >= 95:
    print("Merit")
elif mark >= 80:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print("Fail")