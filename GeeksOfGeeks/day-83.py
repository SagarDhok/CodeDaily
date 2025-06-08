


#! Balanced Array

class Solution:
    def min_value_to_balance(self, arr):
        ln = 0
        for i in arr:
            ln +=1
        mid = ln//2
            

        left =  arr[:mid]
        right = arr[mid:]
        
        left_sum = 0
        for i in left:
          left_sum+=i
        
        
        right_sum = 0
        for j in right:
          right_sum+=j
        
        
        if left_sum>right_sum:
         return left_sum-right_sum
        else:
          return right_sum-left_sum
 
s = Solution()

arr = [int(i) for i in input("Enter list of numbers : ").split()]
print(s.min_value_to_balance(arr))