# In the previous exercise, we hardcoded the values 0 and 100.
# However, it is better to place those values in constants. Therefore, your task is to:
# 1. create a FREEZING_POINT and a BOILING_POINT variable and store the values 0 and 100 in them respectively.
# 2. modify the function of the previous exercise by using those variables instead of the hardcoded 0 and 100 values.
# The previous function is given in the code area.

temperature = float(input("Enter temperature: "))
FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):


    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"


print(water_state(temperature))