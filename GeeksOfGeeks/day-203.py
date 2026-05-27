

#! Count ways with 3 moves
# Difficulty: EasyAccuracy: 43.93%Submissions: 164K+Points: 2
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Return the of count how many possible ways the child can run up the stairs.

# Examples:

# Input: n = 3
# Output: 4
# Explanation: The following are 4 different ways
# 1 step + 1 step + 1 step 
# 1 step + 2 steps 
# 2 steps + 1 step 
# 3 steps
# Input: n = 4
# Output: 7
# Explanation: Below are the 7 ways to reach 4th step:
# 1 step + 1 step + 1 step + 1 step
# 1 step + 2 steps + 1 step
# 2 step + 1 step + 1 step
# 1 step + 1 step + 2 steps
# 2 steps + 2 steps
# 3 steps + 1 step
# 1 step + 3 steps
# Input: n = 1
# Output: 1
# Constraints:
# 1 ≤ n ≤ 30

class Solution:
    def countWays(self, n):
        
        dp = [0] * (n + 1)
        
        dp[0] = 1
        
        for i in range(1, n + 1):
            
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
                
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
                
            if i - 3 >= 0:
                dp[i] += dp[i - 3]
                
        return dp[n]
s = Solution()
n = int(input("Enter A Number : " ))
print(s.countWays(n))