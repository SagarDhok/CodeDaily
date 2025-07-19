

#! Fibonacci in the array
class Solution:
    def countFibonacciNumbers(self, arr):
      max_val = max(arr)
      
      fib_set = set()
      a,b = 0,1
      while a<=max_val:
        fib_set.add(a)
        a,b = b, a + b
        
        
      count = 0
      for i in arr:
         if i in fib_set:
             count+=1
      return count
    
s= Solution()
arr = [4, 2, 8, 5, 20, 1, 40, 13, 23]
print(s.countFibonacciNumbers(arr))

arr = [4, 7, 6, 25]
print(s.countFibonacciNumbers(arr))