def find_words(words,k):
    result = []
    for i in words:
        if len(i) == k:
            result.append(i)
    return result
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
k = 5
long_words = find_words(words, k)
print(f"Words with length {k}: {long_words}")
