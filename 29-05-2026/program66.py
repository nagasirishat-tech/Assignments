import re
def check_special_characters(string):
    pattern = r'[@#$%^&+=]'
    if re.search(pattern, string):
        return "String contains special characters."
    else:
        return "String does not contain special characters."
input_string = input("Enter a string: ")
contains_special = check_special_characters(input_string)
if contains_special:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
