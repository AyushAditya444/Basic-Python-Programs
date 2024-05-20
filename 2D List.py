matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("Full Matrix:")
print(matrix)

print("First Row:")
print(matrix[0])

print("Last Row:")
print(matrix[-1])

print("First 1st Element:")
print(matrix[0][0])

print("Last Last Element:")
print(matrix[-1][-1])

print("Full Matrix In Order:")
for row in matrix:
    for item in row:
        print(item)