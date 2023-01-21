price = 56
txt = "The price is {} dollars"
print(txt.format(price))

txt1 = "The price is {:.2f} dollars"
print(txt1.format(price))

#multiple var
q = 3
itemno = 567
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(q, itemno, price))

#indexes
age = 19
name = "Yerzhan"
txt2 = "His name is {1}. {1} is {0} years old."
print(txt2.format(age, name))

#named indexes
txt3 = "I have a {carname}, it is a {model}."
print(txt3.format(carname = "Toyota", model = "Camry"))