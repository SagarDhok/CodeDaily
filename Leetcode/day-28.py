
# Summary Ranges
def summaryRanges(nums):
    res = []
    if not nums:
        return res

    start = nums[0] 

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            start = nums[i] 

    if start == nums[-1]:
        res.append(str(start))
    else:
        res.append(f"{start}->{nums[-1]}")

    return res

nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))  
