def simple_merge(a, b):
    a, b = sorted(a), sorted(b)  
    merged = []
    i = j = 0
    for _ in range(len(a) + len(b)):
        if j == len(b) or (i < len(a) and a[i] <= b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    return merged
n1 = int(input("How many elements in list1? "))
list1 = [int(input(f"list1[{i}]: ")) for i in range(n1)]
n2 = int(input("How many elements in list2? "))
list2 = [int(input(f"list2[{i}]: ")) for i in range(n2)]
result = simple_merge(list1, list2)
print("Merged sorted list:", result)
