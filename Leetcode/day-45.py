




# Set Mismatch
def findErrorNums(nums):
    seen = set()
    duplicate = -1
    n = len(nums)
    total = n * (n + 1) // 2 
    actual_sum = 0

    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
        actual_sum += num

    missing = total - (actual_sum - duplicate)
    return [duplicate, missing]

print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))
