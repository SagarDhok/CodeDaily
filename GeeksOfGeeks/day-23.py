#find second max from array
class Solution:
    def getSecondLargest(self, arr):
        mv1 = float("-inf")
        mv2 = float("-inf")
        
        for i in arr:
            if i > mv1:
                mv2 = mv1
                mv1 = i
            elif i > mv2 and i != mv1:
                mv2 = i
        
        return mv2 if mv2 != float("-inf") else -1  

sol = Solution()
lst = [int(i) for i in input("Enter List of Values : ").split()]
res  =sol.getSecondLargest(lst)
print(f"Second Largest From {lst} is  : {res}")
