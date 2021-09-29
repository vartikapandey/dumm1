from array import *
arr = array('i', [12, 22, 1, 92, 11, 12, 12, 43, 76, 10])

###accessing array element, done using indexes.
##print(arr[5])
##print(arr[2])

#---insertion---
#insert element at index 5
arr.insert(5, 23)

#insert element at index 1
arr.insert(1, 45)

#---Deletion---
#delete element 22
arr.remove(22)
#delete element 10
arr.remove(10)

#---Search---
#searching can be done using either index or value
#search element 92
print(arr.index(92))
print(arr.index(76))








