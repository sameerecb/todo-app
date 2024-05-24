# Define a get_age function that:
# 1. has two parameters, year_of_birth and current_year .
# 2. the current_year  parameter should be a default parameter. The default value should be the current year.
# 3. the function should calculate and return the age of the user given the year_of_birth and the current_year.

year_of_birth = int(input("Enter your year of birth: "))


def get_age(year_of_birth, current_year=2024):
    current_year = int(2024)
    age = current_year - year_of_birth
    return age


print(f"Your are {get_age(year_of_birth)} year's old")
