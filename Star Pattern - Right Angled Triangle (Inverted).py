int1=int(input("Number of Rows: "))
for i in reversed(range(1,int1+1)):
    for j in reversed(range(1,i+1)):
        print("*",end="")
    print()