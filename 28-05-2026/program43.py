def is_disarium(num):
    str_num = str(num)
    total = 0
    digit_sum=sum(int(digit) for digit in str_num)
    for i, digit in enumerate(str_num):
        total += int(digit) ** (i + 1)
    return total == num
try:
    num = int(input("Enter a number: "))
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Please enter a valid integer.")
