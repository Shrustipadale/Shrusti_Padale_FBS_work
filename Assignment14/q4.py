#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
def findPairs(nums, sum):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == sum:
                pairs.append((nums[i], nums[j]))
    return pairs
nums = list(map(int, input("Enter numbers separated by space: ").split()))
sum = int(input("Enter the target sum: "))
print(findPairs(nums,sum))