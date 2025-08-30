#Write a Python program to find the two numbers whose product isnmaximum among all the pairs in a given list of 
# numbers. Use the Python set.
def Max(nums):
    nums_sorted = sorted(nums)
    prod1 = nums_sorted[0] * nums_sorted[1]
    prod2 = nums_sorted[-1] * nums_sorted[-2]
    if prod1 > prod2:
        return (nums_sorted[0], nums_sorted[1])
    else:
        return (nums_sorted[-2], nums_sorted[-1])

nums = list(map(int, input("Enter numbers separated by space: ").split()))    
print(Max(nums))

