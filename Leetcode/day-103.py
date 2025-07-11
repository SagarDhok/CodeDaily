
#!  Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost) :
            n = len(cost)
            a,b = cost[0],cost[1]
            for i in range(2,n):
                  curr = cost[i]+min(a,b)
                  a,b = b,curr

            return min(a,b)
    
s = Solution()
cost = [10,15,20]
print(s.minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))