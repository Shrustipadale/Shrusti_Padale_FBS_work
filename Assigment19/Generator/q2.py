def palindrome_generator():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

gen = palindrome_generator()
for _ in range(15):
    print(next(gen), end=" ")
