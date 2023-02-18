def gen(n) :
    value = 1
    while value < n:
        if((value * value) <= n) :
            yield value * value 
        value += 1
    

n = int(input())
for x in gen(n):
    print(x)
