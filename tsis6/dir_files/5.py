myList = ["apple", "banana", "cherry"]
with open (r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\test2.txt", "w") as file:
    for x in myList:
        file.write(x+"\n")


cont = open(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\test2.txt")
print(cont.read())