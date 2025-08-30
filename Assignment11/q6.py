list1 = [int(input())  for _ in range(int(input("n1: ")))]
list2 = [int(input()) for _ in range(int(input("n2: ")))]
res = []
for x in list1 + list2:
    if x not in res:
        res.append(x)
for i in range(1, len(res)):
    k = res[i]
    j = i
    while j > 0 and res[j - 1] > k:
        res[j] = res[j - 1]
        j -= 1
    res[j] = k

print(res)

