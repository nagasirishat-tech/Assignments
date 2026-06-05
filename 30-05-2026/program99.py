def replace_vowels(string,char):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        string = string.replace(vowel, char)
    return string
print(replace_vowels("Hello World", "*"))
print(replace_vowels("Python Programming", "#"))
print(replace_vowels("OpenAI ChatGPT", "@"))
