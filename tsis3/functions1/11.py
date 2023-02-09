def palindrome(s):
    for x in range(len(s)):
        if s[x] != s[len(s)-x-1]:
            return False
    return True       

s = input()
is_palindrome = palindrome(s)
if(is_palindrome == False) :
    print(s+" is not palindrome")
else:
    print(s+ " is palindrome")