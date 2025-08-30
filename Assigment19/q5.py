text = input("Enter a string: ")
small_words = [word for word in text.split() if len(word) < 5]
print("Words less than 5 letters:", small_words)
