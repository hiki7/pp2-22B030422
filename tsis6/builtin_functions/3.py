s1 = input()
s2 = ''.join(reversed(s1))

if(s1 == s2):
    print("Palindrome")
else:
    print("Not palindrome")