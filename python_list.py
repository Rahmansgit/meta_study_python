list1 = [1,2,3,4,5]


#print entire list
print(*list1)

#print using seperator
print(list1,sep =" ")

#inserting value at the last, we can insert at the specific point
list1.insert(len(list1), 6)

#another method of inserting
list1.append(7)

#another method of inserting
list1.extend([8,9,10])


print(list1,sep =" ")

#accessing through index
print(list1[2])

list2 = ['A','B','C']

#remove the item accessing through index
list2.pop(2) #index number 2 removed, using index, remember index always starts with '0'

# 'C' has been removed
print(list2, sep =" ")

# another method is delete

del list2[1] # 'B' removed
print(list2, sep =" ")

list3 = ['Hello', 1, True, 40.22]

#list inside a list
list4 = [1, [1, 2, 3], 4]


# iterate the list

for x in list4:
  print('value:',x)
