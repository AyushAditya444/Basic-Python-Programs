Numbers1=[1,2,3,4,5,6,7,8,9,10,2,3,6,8,9]
Numbers2=[]
for i in Numbers1:
    if i not in Numbers2:
        Numbers2.append(i)
print(Numbers2)