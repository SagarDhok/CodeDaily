
#! Exceptionally odd
#APPROACH - 1
class Solution:
    def getOddOccurrence(self, arr):
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in freq:
            if freq[i] % 2 != 0:
                return i
s = Solution()
print(s.getOddOccurrence([1, 2, 3, 2, 3, 1, 3]))
print(s.getOddOccurrence([1, 2, 3, 2, 3, 1, 3]))


#APPROACH - 2
from collections import Counter
class Solution:
    def getOddOccurrence(self, arr):
        freq = Counter(arr)
        print(freq)
        for num, count in freq.items():
            if count % 2 != 0:
                return num
s = Solution()
print(s.getOddOccurrence([1, 2, 3, 2, 3, 1, 3]))
print(s.getOddOccurrence([1, 2, 3, 2, 3, 1, 3]))
