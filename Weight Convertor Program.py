Input1=input("Enter Your Weight: ")
Input2=input("Is Your Weight in (K)g or (L)bs: ")
if Input2=="L" or Input2=="l":
    X=float(Input1)*0.45
    print(f"Your Weight in kg is {X}kg")
elif Input2=="K" or Input2=="k":
    X=float(Input1)/0.45
    print(f"Your Weight in lbs is {X}lbs")
else:
    print("Wrong Input")