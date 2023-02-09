def spy_game(mylist):
    for x in range(len(mylist)-1):
        if mylist[x] == 0:
            for y in range(x+1, len(mylist)):
                if mylist[y] == 0:
                    for z in range(y+1, len(mylist)):
                        if mylist[z] == 7:
                            return True
                else:
                    return False


n = int(input())
mylist = []
for x in range(n):
    m = int(input())
    mylist.append(m)

print(spy_game(mylist))