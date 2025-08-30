text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ''.join([x for x in text if x not in vowels])
print("String without vowels:", result)
