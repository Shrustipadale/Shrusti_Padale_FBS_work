#Python Program to count the occurrences of ach word in a string.

s = input("Enter string: ")
counts = {}
for word in s.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for w, freq in counts.items():
    print(f"'{w}': {freq}")
