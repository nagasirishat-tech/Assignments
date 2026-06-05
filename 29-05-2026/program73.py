sample_dict={'apple': 1, 'banana': 2, 'orange': 3}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Dictionary sorted by keys: ")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")
