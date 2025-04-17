

# Third Maximum Number
def thirdMax(nums):
     nums1 = set(nums)
     nums = list(nums1)
     nums.sort()
     if len(nums)<3:
      return nums[-1]
     return nums[-3]

nums = [int(i) for i in input("Enter List of Values : ").split()]
print("Third Max : ",thirdMax(nums))