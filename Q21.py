numbers = input("Enter a list of numbers separated by spaces: ").split()
element = input("Enter the element to count: ")

numbers = [int(num) for num in numbers]

count = numbers.count(int(element))

print(f"Number of occurrences of {element}: {count}")
