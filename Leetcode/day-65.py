



class Solution:
    def frequencySort(self, nums):
         
        freq = {}
        for i in nums:
         if i not in freq:
           freq[i]=1
         else:
           freq[i]+=1



        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        return sorted_nums
s = Solution()
print(s.frequencySort([1,1,2,2,2,3]))
print(s.frequencySort( [2,3,1,3,2] ))
print(s.frequencySort( [-1,1,-6,4,5,-6,1,4,1]))