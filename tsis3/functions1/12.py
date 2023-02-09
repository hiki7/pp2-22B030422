def histogram(mylist):
    for x in mylist:
        for j in range(x):
            print('*', end="")
        print()
        


n = input()
m = int(n)
mylist = []
for x in range(m):
    i = input()
    j = int(i)
    mylist.append(j)

histogram(mylist)