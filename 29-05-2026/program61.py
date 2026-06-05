def remove_char(input_str,i):
    if i<0 or i>=len(input_str):
        print(f"Index {i} is out of bounds for the input string.")
        return input_str
    result_string = input_str[:i] + input_str[i+1:]
    return result_string

input_str = "Hello, World!"
i = 7
new_str = remove_char(input_str, i)
print(f"String after removing character at index {i}: {new_str}")
print(f"Original string: {input_str}")
