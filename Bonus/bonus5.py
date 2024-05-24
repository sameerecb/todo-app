waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
for index, item in enumerate(waiting_list):
    name = f"{index + 1}. {item.capitalize()}"
    print(name)

##########
## What will the code output this time?

for i, j in enumerate("abcd"):
    print(f"Printing {j * 5}")
##########
## What will the code output this time?
for i, j in enumerate("abcd"):
    print(i + 1)
##########
## What will the code output this time?
for i, j in enumerate("abcd"):
    phrase = f"Printing {i * 5}"
    print(phrase)