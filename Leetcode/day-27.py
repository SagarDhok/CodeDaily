# “Check for Nearby Duplicates Within K Distance”
class Solution:
    def containsNearbyDuplicate(self, nums,k):
        dict = {}
        for idx, val in enumerate(nums):
            if val in dict and idx-dict[val]<=k:
                return True
            else:
                dict[val] = idx
        return False
    
s = Solution()
nums= [int(i) for i in input("Enter List of Values : ").split()]
k = int(input("Enter A number  : "))
res = s.containsNearbyDuplicate(nums,k)
print(res)