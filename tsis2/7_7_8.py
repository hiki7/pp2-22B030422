#making a copy of dictionary by copy() method
dict1 = {
    "phone" : "Xiaomi",
    "cost" : "100$",
    "year" : 2023
}
dict2 = dict1.copy()
print(dict2)

#another way to make a copy is to use built-in dict() function
dict3 = dict(dict1)
print(dict3)

#nested dictionaries consist of several dictionaries
phones = {
    "phone1" : {
        "name" : "Iphone",
        "year" : 2021 
    },
    "phone2" : {
        "name" : "Samsung",
        "year" : 2020
    },
    "phone3" : {
        "name" : "Xiaomi",
        "year" : 2019
    }
}

#