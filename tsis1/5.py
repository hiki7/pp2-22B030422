x = 5
y = "Yerzhan"
print(x)
print(y)

#defining types of variables
a = str(3)    
b = int(3)    
c = float(3)  

#getting type
d = 5
e = "John"
print(type(d))
print(type(e))

#multiple variables
i, j, k = "Orange", "Banana", "Cherry"
print(i)
print(j)
print(k)

#collection
food = ["pizza", "watermelon", "cherry"]
f, g, h = food
print(f)
print(g)
print(h)

#global variables
aw = "awesome"

def myfunc():
  aw = "fantastic"
  print("Python is " + aw)

myfunc()
