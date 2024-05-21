try:
    age=int(input("Enter Your Age: "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Age Cannot Be Zero")
except ValueError:
    print("Wrong Input")