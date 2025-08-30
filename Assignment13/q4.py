# Prompt the user for a number
n = int(input("Enter a number: "))

# Using dictionary comprehension to build the mapping
squares = {x: x * x for x in range(1, n + 1)}

# Output the resulting dictionary
print(squares)
