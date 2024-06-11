choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ").upper()

if choice == 'C':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")
elif choice == 'F':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius}")
else:
    print("Invalid choice.")
