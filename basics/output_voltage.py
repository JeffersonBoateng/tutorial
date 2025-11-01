r1 = float(input("\nEnter resistor R1 (ohms): "))
r2 = float(input("Enter resistor R2 (ohms): "))
vin = float(input("Enter input voltage (volts): "))

vout = vin * (r2 / (r1 + r2))
print(f"The output voltage is: {vout} volts\n")
