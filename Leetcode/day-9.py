
# Find the Unique Element in an Array (Single Number)
nums = [int(i) for i in input("Enter List of Values : ").split()]
for i in nums:
     if nums.count(i)==1:
          print(i)

nums = [int(i) for i in input("Enter List of Values : ").split()]
count  =0
for i in nums:
      count  = count +1 
      if count ==   1:
        print(i)
        break
   
