#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of
#  strings. Use Python set data type.
# Prompt the user to enter text
str = input("Enter some text: ")
words = str.split()

unique_words = set(words)
word_counts = {word: words.count(word) for word in unique_words}
for word, count in word_counts.items():
    print(f"{word}: {count}")
