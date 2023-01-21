a = """sadfsdfsdfsdfsdfsdfsdf
sdfsdfsdfsdfsdfsdfsdfsdf."""
print(a)

#string = array
b = "Some text"
print(b[1])

#loop
for x in "banana":
  print(x)

#length
c = "Hello, World!"
print(len(c))

#if present
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#if not present
txt1 = "The best things in life are free!"
print("expensive" not in txt)

#slicing
d = "Some text"
print(d[2:5])
print(d[:5])
print(d[5:])

#upper
print(d.upper())

#lower
print(d.lower())

#remove whitespace
e = " Some text"
print(e.strip())

#replace
print(d.replace("S", "W"))


