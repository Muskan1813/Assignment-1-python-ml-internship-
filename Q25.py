file1 = "output.txt"
file2 = "output2.txt"

with open(file1, 'r') as source:
    with open(file2, 'w') as destination:
        destination.write(source.read())

print("Contents of",file1, "have been copied to", file2)
