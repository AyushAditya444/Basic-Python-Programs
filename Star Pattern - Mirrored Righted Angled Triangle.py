int1=int(input("Number of Rows: "))
for i in range(1,int1+1):
    for j in range(1, int1-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()