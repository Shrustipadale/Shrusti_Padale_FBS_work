rows=5
for i in range(rows):
    print(''*(rows-i-1),end='')
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
    print()