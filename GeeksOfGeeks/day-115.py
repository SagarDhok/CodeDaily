
#! Friendly Array
class Solution:
    def calculateFriendliness(self, arr):
        n = len(arr)
        total = 0
        for i in range(n):
            total += abs(arr[i] - arr[(i + 1) % n])
        return total

print(Solution().calculateFriendliness([4, 1, 5]))    
print(Solution().calculateFriendliness([1, 1, 1]))    
print(Solution().calculateFriendliness([10, 20, 30]))  
