text = input("Enter a string: ")
character = input("Enter the character to find: ")

positions = []
for i in range(len(text)):
    if text[i] == character:
        positions.append(i)

if positions:
    print(f"The character '{character}' occurs at positions:", positions)
else:
    print(f"The character '{character}' was not found.\n")
