#  Q12
x = int(input("Enter a number: "))
sum_of_digits = 0

while x > 0:
    digit = x % 10
    sum_of_digits += digit
    x = x // 10

print("Sum of the digits:", sum_of_digits)
