# Check password complexity
result = {}
password = input("Enter new password: ")
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase is"] = uppercase
print(result)
if all(result) == True:
    print("You password is strong")
else:
    print("Weak Password")
