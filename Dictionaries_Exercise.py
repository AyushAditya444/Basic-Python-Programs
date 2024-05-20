dict1={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten"
}
input1=input("Enter The Number: ")
input2=""
for i in input1:
    input2=input2+dict1[i]+" "
print(input2)