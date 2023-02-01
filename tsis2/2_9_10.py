#copy a list
list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(list2)

#another way of making a copy by list() method
list2 = list(list1)
print(list2)

#join two lists by "+"
list3 = ["a", "b", "c"]
list4 = [1, 2, 3]
list5 = list3 + list4
print(list5)

#another way using loop
for x in list4 :
    list3.append(x)

print(list3)

#also we can use extend() method which purpose is to add elements from one list to another
list6 = ["d", "e", "f"]
list7 = [4, 5, 6]
list6.extend(list7)
print(list6)

