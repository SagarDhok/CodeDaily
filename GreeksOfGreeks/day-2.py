
#Sum of First N Natural Numbers
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        s = 0
        for val in range(1,n+1):
            s = s+val
            
        print(s)

res = Solution()
res.seriesSum(5)
