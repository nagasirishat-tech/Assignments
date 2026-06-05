def filter_list(lst):
    result = []
    for item in lst:
        if isinstance(item, int) and item >= 0:
            result.append(item)
    return result
filtered_list = filter_list([1, -2, 3, 'a', 4.5, 5])
print(filtered_list)
