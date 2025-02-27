# Write a function that accepts string from user and print all permutations of that string.
def elya(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        elya(s[:i] + s[i+1:], answer + s[i])

san = input("String: ")
elya(san)