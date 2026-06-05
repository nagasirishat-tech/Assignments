def find_n_largest_numbers(lst,n):
    sorted_lst = sorted(lst, reverse=True)
    largest_elements = sorted_lst[:n]
    return largest_elements
numbers=[30,10,45,5,20,50]
N= int(input("N= "))
result=find_n_largest_numbers(numbers,N)
print(f"The {N} largest numbers are: {result}")
