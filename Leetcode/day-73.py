
# Teemo Attacking

class Solution:
    def findPoisonedDuration(self, timeSeries, duration) :
        total = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i+1] - timeSeries[i]
            total += min(duration, gap)
        total += duration 
        return total
    
s = Solution()
timeSeries = [1,4]
duration = 2
print(s.findPoisonedDuration(timeSeries,duration))


timeSeries = [1,2]
duration = 2
print(s.findPoisonedDuration(timeSeries,duration))
