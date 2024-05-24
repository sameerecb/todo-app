# Write a program to ask today date and then ask for how is mood and then write about today.
# File will be created with today's date and same happen everytime you run code on different dates

date = input("Enter today's date: ")
mood = input("How do you rate your mood from 1 to 10 today? ")
thoughts = input("Let your thoughts flow:\n")
with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)


