def double_char(input_string):
    doubled_string = ""
    for char in input_string:
        doubled_string += char * 2
    return doubled_string
# Example usage:
input_str = "Hello"
result = double_char(input_str)
print(result)
