for i in range(5):
    num = float(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)
average = sum(numbers) / len(numbers)
print(f"The average of the five numbers is: {average}\n")
