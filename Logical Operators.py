Input1=input("Is The Person Income is Good (Yes/No): ")
Input2=input("Is The Person Has Good Credit (Yes/No): ")
if Input1=="Yes" and not Input2=="No":
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

Input3=input("Is The Person Income is Good (Yes/No): ")
Input4=input("Is The Person Has Good Credit (Yes/No): ")
if Input3=="Yes" or Input4=="Yes":
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")