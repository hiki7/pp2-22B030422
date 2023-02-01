list1 = ["apple", "banana", "cherry"]
list1[2] = "watermelon"
print(list1)

#change a range of item values
list2 = ["apple", "banana", "cherry", "kiwi", "orange", "mango"]
list2[1:3] = "strawberry", "watermelon"
print(list2)

#insert items
list3 = ["apple", "banana", "cherry", "kiwi", "orange", "mango"]
list3.insert(3, "watermelon")
print(list3)

#extend list
list1 = ["apple", "banana", "cherry"]
temp = ["mango", "pineapple", "papaya"]
list1.extend(temp)
print(list1)

#remove item
list1 = ["apple", "banana", "cherry"]
list1.remove("banana")
print(list1)

#remove item by index
list1 = ["apple", "banana", "cherry"]
list1.pop(2)
print(list1)
list1.pop()
print(list1)

#del
list1= ["apple", "banana", "cherry"]
del list1[0]
print(list1)

#clear empties the list
list1 = ["apple", "banana", "cherry"]
list1.clear()
print(list1)