#This program checks to see if a number is prime or not

number = int(input("Enter a number: "))

if number % 2  == 0 or number % 3 == 0 or number % 5 == 0:
    print(f"{number} is not prime")
else:
    print(f"{number} is prime")