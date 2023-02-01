#arrays 
arr = ["apple", "banana", "cherry"]

#getting access to one of the elements
print(arr[2])

#modifying elements
arr[0] = "watermelon"
print(arr)

#length of an array
print(len(arr))

#loop
for x in arr:
    print(x)

#pop
arr.pop(1)
print(arr)

#also we can use remove method
arr.remove("watermelon")
print(arr)
