


#! Sum Triangle for given array
class Solution:
    def getTriangle(self, arr):
        MOD = 10**9 + 7
        tri = [arr]
        while len(tri[-1]) > 1:
            tri.append([(tri[-1][i] + tri[-1][i+1]) % MOD for i in range(len(tri[-1]) - 1)])
        out = []
        for r in reversed(tri):
            out.extend(r)
        return out
