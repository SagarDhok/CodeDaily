
#  Median of Two Sorted Arrays


def median(nums1, nums2):
    nums3 = nums1 + nums2
    for i in range(len(nums3)):
        for j  in range(i+1,len(nums3)):
            if nums3[i]>nums3[j] :
                nums3[i],nums3[j] = nums3[j],nums3[i]


    n = len(nums3)
    mid = n // 2

    if n % 2 != 0: 
        return nums3[mid]
    else:  
        return (nums3[mid - 1] + nums3[mid]) / 2

nums1 = [0,1,7,9,2,4,3]
nums2 = [8,6,10]
print(median(nums1, nums2))
