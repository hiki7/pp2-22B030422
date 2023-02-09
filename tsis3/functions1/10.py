def unique(mylist):
    temp = []
    for x in mylist:
        if x not in temp:
            temp.append(x)
    return temp

n = int(input())
mylist = []
for x in range(n):
    m = int(input())
    mylist.append(m)

print(unique(mylist))