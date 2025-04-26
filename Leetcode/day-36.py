
#! Next Greater Element I
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = []

for num in nums1:
    idx = nums2.index(num)
    found = -1
    for j in range(idx + 1, len(nums2)):
        if nums2[j] > num:
            found = nums2[j]
            break
    res.append(found)

print(res)  
