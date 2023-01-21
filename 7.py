import random
x = 3    # int
y = 3.4  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#complex numbers
w = 3+5j
print(type(w))

#conversion
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#random numbers
print(random.randrange(1, 20))