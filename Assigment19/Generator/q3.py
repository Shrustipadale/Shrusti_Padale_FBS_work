def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

for num in my_range(1, 10, 2):
    print(num, end=" ")
