#dictionary - collection which is ordered, changeable, and do not allow duplicates
#stores data values in key:value pairs
dict1 = {
    "phone": "Iphone",
    "quantity" : 1,
    "year" : 2021
}
print(dict1)
print(dict1["phone"])

#duplicates values will overwrite existing values
dict2 = {
    "phone": "Iphone",
    "quantity" : 1,
    "year" : 2021,
    "year" : 2022
}
print(dict2)

#length
print(len(dict2))

#values in dictionary can be in different data types
dict3 = {
    "phone": "Iphone",
    "quantity" : 1,
    "year" : 2021,
    "color" : ["pink", "white", "black"]
}
print(type(dict3))

