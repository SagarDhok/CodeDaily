# Find the First Occurrence of an Element in an Array
arr = [int(i) for i in input("Enter List of values : ").split()]
x = int(input("Enter a value : "))
indx = -1
for i in range(len(arr)):
     if x==arr[i]:
       indx = i
       break
print("Index of the value is : ",indx)
  