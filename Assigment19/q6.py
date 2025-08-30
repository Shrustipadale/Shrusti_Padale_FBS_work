sentence = input("Enter a sentence: ")
word_length = {word: len(word) for word in sentence.split()}
print(word_length)
