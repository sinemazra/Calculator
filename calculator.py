print("""
************************************
Welcome to the calculator!

Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
************************************
""")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation number: ")

if operation == "1":
    print("The sum of {} and {} is: {}".format(num1, num2, num1 + num2))

elif operation == "2":
    print("The difference of {} and {} is: {}".format(num1, num2, num1 - num2))

elif operation == "3":
    print("The product of {} and {} is: {}".format(num1, num2, num1 * num2))

elif operation == "4":
    print("The division of {} and {} is: {}".format(num1, num2, num1 / num2))

else:
    print("Invalid Operation.....")