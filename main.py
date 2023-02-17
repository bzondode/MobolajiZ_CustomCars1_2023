# Prints a line of equal signs
print("====================")

# Store Welcome message in a variable
greeting = "Welcome to the UMBC Car Customization Form!"

# Display Welcome message
print(greeting)

# Prints a line of equal signs
print("====================")

# Printing a blank line
print()

# Store instruction(s) for user in a variable
instruction = "(For multiple choice problems, please enter the letter of the selection you're looking for)"

# Display instruction
print(instruction)

# Store info about car in a variable
info = "~ Make & Model ~"

# Display info
print(info)

# Gathering information about user's order and printing
print("1. What Model of Car are you ordering?")
print("  a. Toyota Corolla")
print("  b. Ford Escape")
print("  c. Chevrolet Camaro ")
print("  d. Nissan Rogue")

# Get user's response
response = input("Please enter 'a' - 'd': ")

# Printing a blank line
print()

# Store info about car in a variable
info1 = "~ Weather Package ~"

# Display info
print(info1)

# Gathering information about user's order and printing
print("2. Would you like the deluxe weather package?")
response1 = input("Please enter 'yes' or 'no': ")

# Printing a blank line
print()

# Store info about car in a variable
info2 = "~ Exterior ~"

# Display info
print(info2)

# Gathering information about user's order and printing
print("3. What color would you like your car to be?")
response2 = input("You may enter the name of any color you'd like: ")

# Printing a blank line
print()

# Store info about car in a variable
info3 = "~ Interior ~"

# Display info
print(info3)

# Gathering information about user's order and printing
print("4. Which Engine would you like your car to have?")
print("  a. I-4 Entry Engine")
print("  b. V-6 Performance Engine")
print("  c. V-8 Extra Performance Engine")
print("  d. Eco Diesel Engine")
print("  e. Fully Electric")

# Get user's response
response3 = input("Please enter 'a' - 'e': ")

# Printing a blank line
print()

# Store info about car in a variable
info4 = "~ Heating ~"

# Display info
print(info4)

# Gathering information about user's order and printing
print("5. Would you like heated seats?")
response4 = input("Please enter 'yes' or 'no': ")

# Printing a blank line
print()

# Store info about car in a variable
info5 = "~ Door Style ~"

# Display info
print(info5)

# Gathering information about user's order and printing
print("6. Would like the 4-door option to the 2-door option?")
response5 = input("Please enter 'yes' or 'no': ")

# Printing a blank line
print()

# Prints a line of equal signs
print("====================")

# Display Summary

print("~ Summary ~")
print(f"Model Option: {response}")
print(f"Weather Package: {response1}")
print(f"Desired Color: {response2}")
print(f"Engine Type: {response3}")
print(f"Upgrade to Heated Seats: {response4}")
print(f"Door Style: {response5}")