#Python Program to count number of digits and letters in a string.
s = input("Enter string: ")
letter_count = 0
digit_count = 0

for ch in s:
    if ch.isalpha():
        letter_count += 1
    elif ch.isdigit():
        digit_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)
