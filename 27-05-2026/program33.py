def find_largest_number(array):
    if not array:
        return None  # Return None for an empty array

    largest = array[0]  # Initialize largest with the first element

    for num in array:
        if num > largest:
            largest = num  # Update largest if current number is greater

    return largest
# Example usage
numbers = [3, 5, 7, 2, 8]
largest_number = find_largest_number(numbers)
print(f"The largest number in the array is: {largest_number}")
