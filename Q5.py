# Q5
x = input("Please enter the string you want to write to the file: ")
filename = "output.txt"
with open(filename, 'w') as file:
    file.write(x)
print(f"The string has been written to {filename}")
