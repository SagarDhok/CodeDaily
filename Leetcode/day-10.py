
# Majority Element
nums = [2,2,1,1,1,2,2]
candidate = None
count = 0

for num in nums:
     if count == 0:
          candidate = num
     count += (1 if num == candidate else -1)
print(candidate)