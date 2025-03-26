
# Merge Two Sorted Arrays In-Placed
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums3  = []
for i in range(m):
     nums3.append(nums1[i])

for j in range(n):
     nums3.append(nums2[j])

nums3.sort()

for val in range(len(nums3)):
     nums1[val]=nums3[val]
print(nums1)


