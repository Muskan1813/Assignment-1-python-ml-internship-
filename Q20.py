numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

total_sum = sum(numbers)

print("Sum of the numbers:", total_sum)
