
# Missing Number
nums = [0,3,1]
n = len(nums)
s = 0
for i in range(n+1):
   s += i

array_sum = sum(nums)  

missing_value = s-array_sum
print(missing_value)
