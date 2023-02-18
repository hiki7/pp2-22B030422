def gen(n):
    x = n
    while x >= 0:
        yield x
        x -= 1

n = int(input())
print(*gen(n))