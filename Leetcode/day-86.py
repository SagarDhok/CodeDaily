

# Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums) -> int:
        dct = {}

        for i in nums:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
        
        max_lenght = 0
        for val in dct:
            if val+1 in dct:
                max_lenght= max(max_lenght,dct[val]+dct[val+1])
        return max_lenght
    
s = Solution()
nums = [1,3,2,2,5,2,3,7]
print(s.findLHS(nums))

nums = [1,2,3,4]
print(s.findLHS(nums))

