from Bonus.converter import converter
from Bonus.parsers12 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = converter(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
if result < 1:
    print("Your kid is not allowed to play")
else:
    print("Enjoy with your kids")


