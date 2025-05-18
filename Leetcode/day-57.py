
# Height Checker
class Solution:
    def heightChecker(self, heights):
        expected = heights[::]
        expected.sort()


        i=0
        count = 0
        while i<len(heights) and i<len(expected):
                        if heights[i]!=expected[i]:
                                count+=1
                        i +=1 
        return count
    
s = Solution()
print(s.heightChecker([1,1,4,2,1,3]))
print(s.heightChecker([5,1,2,3,4]))