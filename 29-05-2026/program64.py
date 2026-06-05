def uncommon_words(s1, s2):
    words1 = set(s1.split())
    words2 = set(s2.split())
    
    uncommon_words_set=words1.symmetric_difference(words2)
    uncommon_words_list=list(uncommon_words_set)
    return uncommon_words_list
s1 = "hello world"
s2 = "hello python"
result = uncommon_words(s1, s2)
print("Uncommon words:", result)
