def is_palindrome(s):
    return s == s[::-1]

word = input()
print(is_palindrome(word))  # True
