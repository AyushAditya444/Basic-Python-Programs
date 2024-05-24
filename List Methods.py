Numbers=[2,4,6,8,10]

#To add an element at the end of the list
Numbers.append(12)
print(Numbers)

#To remove last element from the list
Numbers.pop()
print(Numbers)

#To add an element at the beginning of the list
Numbers.insert(0,1)
print(Numbers)

#To remove an element from the list
Numbers.remove(2)
print(Numbers)

#To sort the list
Numbers.sort()
print(Numbers)

#Copy A List
Numbers2=Numbers.copy()
print(Numbers2)

#To reverse the list
Numbers.reverse()
print(Numbers)

#To print the list
print(Numbers)

#To print the length of the list
print(len(Numbers))

#To print the index of an element
print(Numbers.index(6))

#To print the count of an element
print(Numbers.count(10))

#If Number Exists in List
print(10 in Numbers)

#To clear the list
Numbers.clear()
print(Numbers)