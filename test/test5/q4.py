list1=[1,3,4,1,2,3,6,7,1,2,4]
freqdict={}
for num in list1:
    if num in freqdict:
        freqdict[num]+=1
    else:
        freqdict[num]=1
print(freqdict)
