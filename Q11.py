# Q11
n = int(input("Enter the number : "))

fib_seq = []

a, b = 0, 1
for _ in range(n):
    fib_seq.append(a)
    a, b = b, a + b

print(fib_seq)
