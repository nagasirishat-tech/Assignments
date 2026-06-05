def is_binary_string(input_string):
    for char in input_string:
        if char not in ['0', '1']:
            return False
    return True
input_string = "1010101"
if is_binary_string(input_string):
    print(f"{input_string} is a binary string.")    
else:
    print(f"{input_string} is not a binary string.")
