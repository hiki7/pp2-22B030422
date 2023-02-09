#adding new items
dict1 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
dict1["color"] = "white"
print(dict1)

#items can be addee=d by using update()
dict2 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
dict2.update({"color": "black"})
print(dict2)

#removing items by several methods
#pop() remove item with the specified key name
dict3 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
dict3.pop("year")
print(dict3)

#popitem() removes the last added item
dict4 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
dict4.popitem()
print(dict4)

#del removes the item with the specified key name
dict5 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
del dict5["cost"]
print(dict5)

#clear() empties the dictionary
dict6 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
dict6.clear()
print(dict6)

#loop through a dictionary
#first of all we want to print key names
dict7 = {
    "phone": "Samsung",
    "cost" : "200$",
    "year": 2021
}
for x in dict7:
    print(x)

#printing all VALUES in the dictionary
for x in dict7:
    print(dict7[x])

#instead of the code above we can use values() method
for x in dict7.values() :
    print(x)

#instead of the first code of loop we can use keys() method
for x in dict7.keys() :
    print(x)

#we can print both keys and values by using the items() method
for x, y in dict7.items() :
    print(x, y)


 