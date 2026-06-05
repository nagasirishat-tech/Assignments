def index_of_caps(word):
    return [i for i, c in enumerate(word) if c.isupper()]
print(index_of_caps("HeLloWorLD"))
print(index_of_caps("Python"))
