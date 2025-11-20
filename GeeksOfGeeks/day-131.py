
#! Union of Arrays with Duplicates
class Solution:
    def findUnion(self, a, b):
        s = set()
        for x in a:
            s.add(x)
        for x in b:
            s.add(x)
        return sorted(list(s))


s = Solution()
a= [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(s.findUnion(a,b))

a = [1, 2, 3]
b = [4, 5, 6] 
print(s.findUnion(a,b))

a = [1, 2, 1, 1, 2]
b = [2, 2, 1, 2, 1] 
print(s.findUnion(a,b))
