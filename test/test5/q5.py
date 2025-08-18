l1=[1,2,3,4,5]
l2=[4,5,6,8,9]
union_list=[]
for item in l1:
    if item not in union_list:
        union_list.append(item)

for item in l2:
    if item not in union_list:
        union_list.append(item)
        

print(union_list)