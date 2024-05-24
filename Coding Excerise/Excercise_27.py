# Define a function that calculates the area of a square.
# For example, if I was to call your function with foo(7) the output would be 49. If I called it with foo(3)
# it would return 9, and so on. Note that you don't have to name your function foo. Give it any name you want.


def area_of_square(number):
    area = number * number
    return area


user_input = float(input("Enter the size of your square wall: "))
area = area_of_square(user_input)
print(area)
