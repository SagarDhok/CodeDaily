# Intersection of Two Arrays II
class Solution:
    def intersection(self, nums1, nums2):
       n2 = nums2[:]  
       lst = []

       for i in nums1:
            if i in n2:
                lst.append(i)
                n2.remove(i)  
       return lst
s= Solution()
nums1 = [1, 2, 2, 2]
nums2 = [2]
print(s.intersection(nums1,nums2))
