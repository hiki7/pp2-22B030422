def gen(n):
    for x in range(0, n+1):
        if (x % 2) == 0:
            yield x


n = int(input())
print(*gen(n), sep=", ")