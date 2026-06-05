def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"
print(correct_signs("2 + 3 * (4 - 1)")) 
print(correct_signs("10 / 2 + 5"))
print(correct_signs("5 * (2 + 3) - 4"))
