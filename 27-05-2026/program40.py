str=input("Enter a string: ")
words=[word.capitalize() for word in str.split()]
words.sort()
print("Sorted words:")
for word in words:
    print(word)
