import random

print("Welcome to the Random Number Generator!")

lower_number = int(input("Enter the lower bound of the range: "))
upper_number = int(input("Enter the upper bound of the range: "))

if lower_number < upper_number:
    random_number = random.randint(lower_number, upper_number)
    print(f"Random number between {lower_number} and {upper_number} is: {random_number}")
else:
    print("Lower bound must be less than the upper bound.")