#while loop
i = 1
while i < 7:
    print(i, end=" ")
    i += 1
print()

#adding break to loop
j = 1 
while j < 7:
    print(j, end=" ")
    if j == 4 :
        break
    j += 1
print()

#continue in loop
k = 0
while k < 6:
    k += 1
    if k == 4 :
        continue
    print(k, end=" ")
print()

#else statement
x = 1
while x < 7 :
    print(x, end=" ")
    x += 1
else : 
    print()
    print("x is no longer less than 7")

