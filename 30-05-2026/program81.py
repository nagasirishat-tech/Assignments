class DivisibleBySeven:
    def __init__(self, number):
        self.number = number

    def generate_divisible_by_seven(self):
        for num in range(self.number + 1):
            if num % 7 == 0:
                yield num
n=int(input("Enter a number: "))
divisible_by_seven = DivisibleBySeven(n).generate_divisible_by_seven()
print(f"Numbers divisible by 7 up to {n}:")
