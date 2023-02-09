def reverse(s):
    words = s.split()
    words.reverse()
    for x in words:
        print(x, end=" ")

s = input()
reverse(s)