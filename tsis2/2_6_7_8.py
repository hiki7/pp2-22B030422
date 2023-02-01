list1 = ["apple", "banana", "cherry"]
for x in list1:
    print(x)

#loop through the index numbers
for i in range(len(list1)) :
    print(list1[i])

#while loop
j = 0
while j < len(list1) :
    print(list1[j])
    j = j + 1

#loop using list comprehension
[print(y) for y in list1]

#list comprehension -> shorter syntax
#without it code will look like this
list2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for z in list2 :
    if 'a' in z :
        newlist.append(z)

print(newlist)

#with list comprehension
newlist = [z for z in list2 if 'a' in z]
print(newlist)

#conditions in list comprehension
newlist1 = [x for x in list2 if x != 'apple']
print(newlist1)

#iterable - any object (list, tuple, set etc)
#range can be used for creating iterable
newlist2 = [x for x in range(10)]
print(newlist2)

#range with condition
newlist2 = [x for x in range(10) if x < 5]
print(newlist2)

#expression is the current item in iteration
newlist3 = [x.upper() for x in list2]
print(newlist3)

newlist3 = ["hello" for x in list2]
print(newlist3)

#expression can also contain conditions
newlist3 = [x if x != "banana" else "orange" for x in list2]
print(newlist3)

#sort list alphanumerically (ascending by default)
list2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list2.sort()
print(list2) 

#sort the list numerically
list3 = [100, 50, 5, 10, 25]
list3.sort()
print(list3)

#sort in descending order
list2.sort(reverse = True)
print(list2)

list3.sort(reverse = True)
print(list3)

#customize sort function
def myf(n) :
    return abs(n - 50)

list3.sort(key = myf)
print(list3)

#case sensitive sort - capital letters will be sorted before lower case letters
list4 = ["Apple", "orange", "banana", "Kiwi"]
list4.sort()
print(list4)

#case insensitive function
list4.sort(key = str.lower)
print(list4)

#reverse order
list4.reverse()
print(list4)