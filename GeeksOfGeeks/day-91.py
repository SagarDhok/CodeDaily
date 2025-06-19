
# Positive and negative elements

class Solution:
    def arranged(self,arr):
        pos = [i for i in arr if i>=0 ]
        neg = [i for i in arr if i<=0]
        
        
        i = 0
        j = 0
        result = []
        while i<len(pos) and j<len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i+=1
            j+=1
        return result
            
s = Solution()
arr = [-1, 2, -3, 4, -5, 6]
print(s.arranged(arr))

arr = [-3, 2, -4, 1]
print(s.arranged(arr))



arr = [2,-18]
print(s.arranged(arr))
