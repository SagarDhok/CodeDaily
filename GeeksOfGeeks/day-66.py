
# Mega Sale
class Solution:
    def maxProfit(self, m, arr):
     usless_laptop = [i for i in arr if i<0]

     usless_laptop.sort()

    
     s  = 0
     for i in range(min(m, len(usless_laptop))):
        s += abs(usless_laptop[i])
     return s
s = Solution()
m = 3
arr = [-6, 0, 35, 4]
profit = s.maxProfit(m, arr)
print(f"Maximum profit from returning up to {m} useless laptops is: {profit}")


m = 2
arr = [1, -2, -3, -4, 5]
profit = s.maxProfit(m, arr)
print(f"Maximum profit from returning up to {m} useless laptops is: {profit}")
