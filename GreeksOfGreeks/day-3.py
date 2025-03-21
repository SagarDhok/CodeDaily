# Find the Maximum Element in an Array (Without Using Functions)
arr = [int(i) for i in input("Enter List of values  : ").split()]
mv1 = float("-inf")
for i in arr:
  if i>mv1:
     mv1 = i
print("Largest Element is : ",mv1)

