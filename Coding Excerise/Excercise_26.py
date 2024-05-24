# Write a get_nr_items function that:
# 1. gets as a parameter one string with commas. E.g., "john,lisa, teresa"
# 2. the function should return the number of items divided by commas in that string
# (i.e., that would be three items in the above example)
# 2. returns the number of items.


def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)


user_input = input("Enter user name with commas: ")
nr_items = get_nr_items(user_input)
print(nr_items)

