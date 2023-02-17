import math

numberOfSides = float(input("Input number of sides: "))
length = float(input("Input the lenght of a side: "))
area = (numberOfSides * math.pow(length, 2)) / (4 * math.tan(math.pi / numberOfSides))
print("The area of the polygon is:", round(area))