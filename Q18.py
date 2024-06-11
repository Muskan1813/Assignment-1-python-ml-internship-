string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

cleaned_string1 = string1.replace(" ", "").lower()
cleaned_string2 = string2.replace(" ", "").lower()

if sorted(cleaned_string1) == sorted(cleaned_string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
