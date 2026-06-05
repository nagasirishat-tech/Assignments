def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "Bool value expected"
print(reverse(True))
