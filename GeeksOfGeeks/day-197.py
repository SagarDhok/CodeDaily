


#! Print n to 1 without loop
# Difficulty: EasyAccuracy: 77.72%Submissions: 137K+Points: 2Average Time: 10m
# Print numbers from n to 1 (space separated) without the help of loops.

# Examples :

# Input: n = 10
# Output: 10 9 8 7 6 5 4 3 2 1
# Constraints :
# 1 ≤ n ≤ 1000


class Solution:
    def printNos(self, n):
        if n==0:
            return 
        
        print(n,end =" ")
        self.printNos(n - 1)

s = Solution()
n = int(input("Enter A Number  : "))
print(s.printNos(n))