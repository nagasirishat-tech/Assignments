def is_harshed_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0 
num=int(input("Enter a number: "))  
if is_harshed_number(num):
    print(f"{num} is a Harshad number.")    
else:    print(f"{num} is not a Harshad number.")
