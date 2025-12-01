


#! 997. Find the Town Judge

class Solution:
    def findJudge(self, n, trust):
        trusts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1


s = Solution()
n = 2
trust = [[1,2]]
print(s.findJudge(n,trust))


n = 3
trust = [[1,3],[2,3]]
print(s.findJudge(n,trust))

n = 3
trust = [[1,3],[2,3],[3,1]]
print(s.findJudge(n,trust))