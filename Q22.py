numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

min_value = min(numbers)
max_value = max(numbers)

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
