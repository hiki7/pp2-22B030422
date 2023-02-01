#remove by remove() or discard() methods
set1 = {"apple", "banana", "cherry"}
set1.remove("apple")
set1.discard("cherry")
print(set1)

#pop() will delete random value
set2 = {"apple", "banana", "cherry"}
x = set2.pop()
print(x)
print(set2)

#clear set
set3 = {"apple", "banana", "cherry"}
set3.clear()
print(set3)

#loop
set4 = {"apple", "banana", "cherry"}
for x in set4:
    print(x)

#join two sets using union or update
set5 = {"a", "b", "c"}
set6 = {1, 2, 3}
set7 = set5.union(set6)
print(set7)

myset1 = {"e", "f", "g"}
myset2 = {4, 5, 6}
myset1.update(myset2)
print(myset1)

#keeping only duplicates 
x = {"apple", "banana", "cherry"}
y = {"facebook", "netflix", "apple"}

x.intersection_update(y)

print(x)

#intersection() method will return NEW SET
z = x.intersection(y)
print(z)

#keep all, but not the duplicates
x.symmetric_difference_update(y)
print(x)

#symmetric_difference() will return NEW SET
x = {"apple", "banana", "cherry"}
y = {"facebook", "netflix", "apple"}
w = x.symmetric_difference(y)
print(w)