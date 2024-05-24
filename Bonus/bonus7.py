filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)

# Check code below and write another code for same results
new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)

# New code
old = [1, 2 ,3 ]
new = [i + 10 for i in old]
print(new)

# What output will the following code produce?

new = [i for i in ['a', 'b', 'c']]
print(new)