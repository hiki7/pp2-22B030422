def tt(mylist):
    for x in range(len(mylist) - 1):
        if mylist[x:x+2] == [3, 3]:
            return True
    return False
        

n = int(input())
mylist = []
for x in range(n):
    i = int(input())
    mylist.append(i)

print(tt(mylist))