
# "Greedy Algorithm: Assign Cookies to Maximize Content Children"
class Solution:
    def findContentChildren(self, g, s) :
        g.sort()
        s.sort()

        i = 0
        j = 0
        count = 0

        while i < len(g) and j < len(s):
            if g[i]<=  s[j]:
                count += 1
                i += 1
            j += 1

        return count

sol = Solution()
print(sol.findContentChildren([1, 2, 3], [1, 1]))  
print(sol.findContentChildren([1, 3], [1, 2, 3])) 

