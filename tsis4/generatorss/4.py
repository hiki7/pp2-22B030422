def squares(a, b):
    for x in range(a, b+1):
        yield x * x


a = int(input())
b = int(input())
for x in squares(a, b):
    print(x)