feet_inches = input("Enter feet and inches: ")


def converter(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters
    # return f"{feet} feet and {inches} inches is equal to {meters} meters."


result = converter(feet_inches)
if result < 1:
    print("Your kid is not allowed to play")
else:
    print("Enjoy with your kids")


