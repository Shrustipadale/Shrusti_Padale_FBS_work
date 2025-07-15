rows = 4  

for i in range(1, rows + 1):
    
    print('  ' * (rows - i), end='')  

    
    C = 1
    for j in range(1, i + 1):
        print(C, end='  ')
        C = C * (i - j) // j

    print()  