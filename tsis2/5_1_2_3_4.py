#tuple - collection which is ordered and unchangeable
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

#tuples allow duplicates
tuple2 = ("apple", "apple", "banana")
print(tuple2) 

#length
print(len(tuple1))

#one item tuple
tuple3 = ("apple",)
print(type(tuple3))

#not a tuple
ntuple = ("apple")
print(type(ntuple))

#access tuple
print(tuple1[2:])
tuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple4[-3:-1])

#change tuple values. tuple -> list, change values in list, list -> tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "watermelon"
x = tuple(y)
print(x)

#add items
z = ("apple", "banana", "cherry")
w = list(z)
w.append("orange")
z = tuple(w)
print(z)

z = ("apple", "banana", "cherry")
k = ("watermelon",)
z += k
print(z)

#remove
z = ("apple", "banana", "cherry")
j = list(z)
j.remove("apple")
z = tuple(j)
print(z)

#unpacking tuples - we are allowed to extract the values back into variables
z = ("apple", "banana", "cherry")
(green, yellow, red) = z
print(green)
print(yellow)
print(red)

#using asterisk - if the number of variables is less than number of values in tuple, than we can use * at the end of variable, then these values will be assigned to the variable as a list
tuple5 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(blue, black, *white) = tuple5
print(blue)
print(black)
print(white)

(pink, *grey, brown) = tuple5
print(pink)
print(grey)
print(brown)

