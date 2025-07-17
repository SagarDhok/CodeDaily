

#! Even occurring elements
class Solution:
    def findEvenOccurrences(self, arr):
        
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        
        res = []
        for j in freq:
            if  freq[j]%2==0:
                res.append(j)
         
        return res if res else [-1]

s = Solution()
arr = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
print(s.findEvenOccurrences(arr))

arr = [23, 12, 56, 34, 32]
print(s.findEvenOccurrences(arr))