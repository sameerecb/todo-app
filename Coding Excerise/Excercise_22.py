# Create a liters_to_m3 function that:
#
# 1. gets a liters parameter
#
# 2. converts liters to cubic meters knowing that 1000 liters are
# equal to 1 cubic meter and returns the cubic meters.
# Note: Defining the function is enough. You do not need to call or
# print out a function output, but you should name the function exactly liters_to_m3.

liters = float(input("Enter amount in liters: "))


def liters_to_m3():
    m3 = liters / 1000
    return m3


print(liters_to_m3())
