def move_to_end(lst,element):
    count = lst.count(element)
    lst = [x for x in lst if x != element]
    lst.extend([element]*count)
    return lst
print(move_to_end([1, 2, 3, 4, 5], 3))
print(move_to_end([1, 2, 3, 4, 5], 6))
