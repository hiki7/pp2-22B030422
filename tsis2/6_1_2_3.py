#sets - collection which is unordered, unchangeable, and unindexed
myset = {"apple", "orange", "banana"}
print(myset)

#duplicates not allowed
myset2 = {"apple", "apple", "banana", "orange"}
print(myset2)

#length
print(len(myset2))

#set contains values with different data types
myset1 = {"abc", 123, True, 3j}
print(myset1)

#type
print(type(myset1))

#access items
for x in myset1:
    print(x)

#check if item is present in the set
print("abc" in myset1)

#add items
myset4 = {"apple", "banana", "cherry"}
myset4.add("watermelon")
print(myset4)

#add items from one set to another
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#update() can be used for any iterable
set3 = {"d", "e", "f"}
list1 = ["g", "h"]
set3.update(list1)
print(set3) 