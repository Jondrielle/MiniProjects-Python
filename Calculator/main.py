#Calculator project

num1 = float(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter a number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("This is not a correct operation symbol. Please you either +, -, /, %, or *.")
