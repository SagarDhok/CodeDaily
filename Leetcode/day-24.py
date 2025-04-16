
#  Median of Two Sorted Arrays


def median(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()
    n = len(nums3)
    mid = n // 2

    if n % 2 != 0: 
        return nums3[mid]
    else:  
        return (nums3[mid - 1] + nums3[mid]) / 2

nums1 = [1, 3]
nums2 = [2]
print(median(nums1, nums2))
