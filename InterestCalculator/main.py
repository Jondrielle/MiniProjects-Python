#This program calculates simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate as a decimal: "))
timePeriod = float(input("Enter time period: "))

amount = float(principal * (1 + (rate * timePeriod)))
print(f"${amount} is the total you have accured per year for {timePeriod} years.")