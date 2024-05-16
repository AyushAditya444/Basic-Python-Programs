print("Price Of The House Is 1Million")
Credit=input("Do You Have Good Credit Score (Yes/No): ")
if Credit=="Yes" or Credit=="yes":
    print("You Need to put 10% Downpayment")
    print(int(1000000*0.1))
else:
    print("You Need to put 20% Downpayment")
    print(int(1000000*0.2))