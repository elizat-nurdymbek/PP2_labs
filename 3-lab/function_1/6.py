# Write a function that accepts string from user, 
# return a sentence with the words reversed.
# We are ready -> ready are We

def reverse_coz(sentence):
    return " ".join(sentence.split()[::-1])

s = input("Sentence: ")
print(reverse_coz(s))