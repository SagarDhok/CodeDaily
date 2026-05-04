

class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: x[1], reverse=True)
        
        max_deadline = max(deadline)
        slots = [-1] * (max_deadline + 1)
        
        count = 0
        total_profit = 0
        
        for d, p in jobs:
            for i in range(d, 0, -1):
                if slots[i] == -1:
                    slots[i] = p
                    count += 1
                    total_profit += p
                    break
        
        return [count, total_profit]
s = Solution()
deadline = [4, 1, 1, 1]
profit = [20, 10, 40, 30]
print(s.jobSequencing(deadline,profit))


class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: x[1], reverse=True)
        
        max_deadline = max(deadline)
        parent = [i for i in range(max_deadline + 1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            parent[u] = v
        
        count = 0
        total_profit = 0
        
        for d, p in jobs:
            available = find(d)
            if available > 0:
                union(available, find(available - 1))
                count += 1
                total_profit += p
        
        return [count, total_profit]
deadline = [4, 1, 1, 1]
profit = [20, 10, 40, 30]
print(s.jobSequencing(deadline,profit))
