x=9
y=1
while y<=3:
    z=int(input("Enter Your Guess: "))
    if x==z:
        print("You Win")
        break
    else:
        print("Try Again")
        y=y+1
if y==4:
    print("You Lose")