#loop
tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
    print(x)

#loop through indexes
for x in range(len(tuple1)):
    print(tuple1[x])

#while loop
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i = i + 1

#join two tuples
tuple2 = ("a", "b", "c")
tuple3 = (1, 2, 3)
tuple4 = tuple2 + tuple3
print(tuple4)

#multiply tuples
newtuple = tuple2 * 3
print(newtuple)

