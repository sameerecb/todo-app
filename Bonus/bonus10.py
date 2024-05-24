try:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    if length == width :
        exit("That looks like a square, entry rectangle details")
    area = width * length
    print("The area of rectangle is: ", area)
except ValueError:
    print("Please enter a digit/number")
