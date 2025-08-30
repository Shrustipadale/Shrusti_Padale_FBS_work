divisible_nums = [x for x in range(1, 1001) if True in [x % y == 0 for y in range(2, 10)]]
print(divisible_nums)
