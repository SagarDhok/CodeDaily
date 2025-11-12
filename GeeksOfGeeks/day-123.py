

class Solution:
    def findMaxOddSum(self, arr):
        total = 0
        min_odd_pos = float('inf')
        max_odd_neg = float('-inf')
    
        for x in arr:
            if x > 0:
                total += x
                if x % 2 != 0:
                    min_odd_pos = min(min_odd_pos, x)
            elif x % 2 != 0:
                max_odd_neg = max(max_odd_neg, x)
    
        if total % 2 != 0:
            return total
    
        option1 = total - min_odd_pos if min_odd_pos != float('inf') else float('-inf')
        option2 = total + max_odd_neg if max_odd_neg != float('-inf') else float('-inf')
    
        result = max(option1, option2)
        return result if result != float('-inf') else -1

s = Solution()
arr = [4, -3, 3, -5]
print(s.findMaxOddSum(arr))

arr = [2, 5, -4, 3, -1]
print(s.findMaxOddSum(arr))