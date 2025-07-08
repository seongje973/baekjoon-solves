def is_palindrome(s):
    return s == s[::-1]

s = input()
for i in range(len(s)):
    if is_palindrome(s[i:]):
        print(len(s) + i)
        break