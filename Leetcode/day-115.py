

#! Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1,nums2) :
        full_array = nums1+nums2
        full_array.sort()
        
        n = len(full_array)
        mid = n//2

        if n % 2 == 1:
            return full_array[mid]
        else:
            return (full_array[mid - 1] + full_array[mid]) / 2
        
s = Solution()
nums1 = [1,3]
nums2 = [2]
print(s.findMedianSortedArrays(nums1,nums2))

nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1,nums2))