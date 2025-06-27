

#! Difference between highest and lowest occurrence
class Solution:
    def findDiff(self, arr):
        freq_count = {}

        for i in arr:  
          if i not in freq_count:
            freq_count[i]=1
          else:
            freq_count[i]+=1
        
        
        max_freq = max(freq_count.values())
        min_freq = min(freq_count.values())
        
        return max_freq-min_freq


s = Solution()
print(s.findDiff([int(i) for i in input("Enter The Elements Of Array : ").split()]))
