list1 = ["apple", "cherry", "banana"]
for x in list1 :
    print(x)

#loop through string
for x in "banana":
    print(x)

#break statement
list2 = ["apple", "banana", "cherry"]
for x in list2:
    print(x)
    if x == "banana":
        break

for x in list2:
    if x == "banana":
        break
    print(x)

#continue
for x in list2:
    if x == "apple":
        continue
    print(x)

#range function
for x in range(6):
    print(x)

for x in range(3, 6):
    print(x)

#specifying increment
for x in range(2, 30, 4):
    print(x)

#else
for x in range(6):
    print(x)
else:
    print("Loop is finished")

#if loop breaks then else will not work
for x in range(6):
    if x == 4: break
    print(x)
else:
    print("Finished")

#nested loops - one loop in another
list3 = ["red", "small", "tasty"]
list4 = ["apple", "banana", "cherry"]
for x in list3:
    for y in list4:
        print(x, y)

#with pass we can avoid errors in empty loop
for x in [1, 2, 3]:
    pass