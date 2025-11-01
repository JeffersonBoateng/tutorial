principal = float(input("Enter the principal amount:\n "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
print(f"The simple interest after {time} years is: {simple_interest}\n")
