def cube_sum_of_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    else:
        total=sum([i**3 for i in map(int, str(n))])
    return total

n = int(input("Enter a value: "))
if n <= 0:
    print("Input must be a non-negative integer.")
else:
    result = cube_sum_of_digits(n)
    print(f"The sum of cubes of digits of {n} is {result}.")
