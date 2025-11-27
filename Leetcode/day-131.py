

#! 961. N-Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, nums) :
        n = len(nums)/2
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for k,v in freq.items():
            if n==v:
                return k
s  = Solution()
nums = [1,2,3,3]
print(s.repeatedNTimes(nums))

nums = [2,1,2,5,3,2]
print(s.repeatedNTimes(nums))

nums = [5,1,5,2,5,3,5,4]
print(s.repeatedNTimes(nums))