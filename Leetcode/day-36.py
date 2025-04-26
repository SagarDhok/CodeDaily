
#! Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        
        for num in nums1:
            idx = nums2.index(num)
            found = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    found = nums2[j]
                    break
            res.append(found) 
        
        return res

sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2])) 
