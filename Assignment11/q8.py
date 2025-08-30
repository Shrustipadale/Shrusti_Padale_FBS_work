import copy
list1 = []
main = []
row = 1
for i in range(1, 101):
    list1.append(i)
    if i % 10 == 0:
        if row % 2 == 0:
            list1.reverse()
        main.append(copy.deepcopy(list1)) 
        row += 1
        list1.clear()
main.reverse()
for row in main:
    print(*row)
