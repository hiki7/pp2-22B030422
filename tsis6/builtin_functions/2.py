s = input()
upper_count = 0
lower_count = 0

for i in s:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1


print("Number of upper case letters in string =", upper_count)
print("Number of lower case letters in string =", lower_count)