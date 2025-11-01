resistance = float(input("Enter resistance (ohms):\n "))
capacitance = float(input("Enter capacitance (farads):\n "))

time_constant = resistance * capacitance
print(f"The time constant of the RC circuit is: {time_constant} seconds.\n")
