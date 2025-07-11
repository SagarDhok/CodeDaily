
#! Repeated IDs

class Solution:
    def uniqueId(self, arr):
        seen = [False] * 10  
        lst = []
        
        for i in arr:
            if not seen[i]:
                lst.append(i)
                seen[i] = True
        print(seen)        
        return lst
s = Solution()
print(s.uniqueId([int(i) for i in input("Enter Array Elements : ").split()]))