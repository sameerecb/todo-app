# Define a function that:
# (1) takes a string as a parameter
# (2) returns False if the string contains less than 8 characters
# (3) returns True if the string contains 8 or more characters
# In other words, if I called your function with foo("mypass")
# it would return False. If I called it with foo("mylongpassword") it would return True, and so on.


def password_strength(user_input):

    if len(user_input) < 8:
        return False
    else:
        return True


user_input = input("Enter your password: ")
strength = password_strength(user_input)
print(strength)
