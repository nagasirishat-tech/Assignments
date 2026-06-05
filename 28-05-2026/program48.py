def is_pronic_number(n):
    for i in range(1, int(n**0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False
print("Pronic numbers between 1 and 100:")
for n in range(1, 101):
    if is_pronic_number(n):
        print(n, end=" | ")
