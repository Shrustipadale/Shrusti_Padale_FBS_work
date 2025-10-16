def selection_sort(arr):
    try:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    except Exception as e:
        print("Error in sorting:", e)

def binary_search(arr, x):
    try:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    except Exception as e:
        print("Error in searching:", e)

try:
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    nums = selection_sort(nums)
    print("Sorted List:", nums)
    key = int(input("Enter number to search: "))
    pos = binary_search(nums, key)
    if pos != -1:
        print(f"Element found at position {pos + 1}")
    else:
        print("Element not found")
except Exception as e:
    print("Invalid input:", e)