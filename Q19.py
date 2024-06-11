import string
OriginalString = input("Enter a string with punctuation: ")

translator = str.maketrans('', '', string.punctuation)

NewString = OriginalString.translate(translator)

print("String without punctuation:", NewString)
