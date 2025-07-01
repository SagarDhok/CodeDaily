

#! Average Count Array
from collections import Counter
class Solution:
    def countArray (self, arr, x) : 
        freq = Counter(arr)
        
        result = []
        for num in arr:
            avg = (num + x) // 2  
            result.append(freq.get(avg, 0))
        
        return result

s = Solution()
print(s.countArray([int(i) for i in input("Enter Array Elements : ").split()]))