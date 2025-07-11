
#! 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost) :
        cost.append(0)

        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])

        print(cost)
        return min(cost[0],cost[1])


s = Solution()
cost = [10,15,20]
print(s.minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))