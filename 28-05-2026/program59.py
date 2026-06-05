def count_occurences(lst,element):
    count=lst.count(element)
    return count
my_list=[1,2,3,4,5,1,2,1]
element=1
occurences=count_occurences(my_list,element)
print(f"The element {element} occurs {occurences} times in the list.")
