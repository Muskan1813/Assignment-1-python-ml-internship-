lines = []
while True:
    line = input("Enter a line (press Enter to finish): ")
    if line:
        lines.append(line)
    else:
        break
print("Entered lines:")
for line in lines:
    print(line)
