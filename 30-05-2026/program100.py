def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False
print(correct_signs("2 + 3 * 4"))
print(correct_signs("10 / 2 - 5"))
print(correct_signs("5 + (3 * 2)"))
