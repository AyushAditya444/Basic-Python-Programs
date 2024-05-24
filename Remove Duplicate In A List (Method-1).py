Numbers=[1,2,3,4,5,6,7,8,9,10,2,3,6,8,9]
for i in Numbers:
    if Numbers.count(i)>1:
        Numbers.remove(i)
print(Numbers)