
# Two Sum: Find Indices of Pair Adding to Target
nums= [int(i) for i in input("Enter list values : ").split()]
print("Your List : ",nums)
target = int(input("Enter Your Target : "))
for i in range(len(nums)):
         for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
               print(f"Numbers : ({nums[i]} + {nums[j]}) = {target}")
               print(f"Indices : {i} and {j} ")