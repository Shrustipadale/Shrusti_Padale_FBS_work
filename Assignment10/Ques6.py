original = [2, 1, 3, 2, 4, 1, 5]
result = []

for item in original:
    if item not in result:
        result.append(item)

print(result)  # Output: [2, 1, 3, 4, 5]
