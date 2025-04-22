
class Solution:
    def intersection(self, nums1, nums2):
        
       lst = []
       for i in nums1:
         if i in nums2 and i not in lst:
            lst.append(i)
       return lst
 
s= Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersection(nums1,nums2))
