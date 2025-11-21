

#! Second Largest
class Solution:
    def getSecondLargest(self, arr):
            if len(arr) < 2:
              return -1

            largest = second = -1
        
            for num in arr:
                if num > largest:
                    second = largest
                    largest = num
                elif num != largest and num > second:
                    second = num
        
            return second
           
s = Solution()
arr = [int(i) for i in input("Enter Arr Values : ").split()]
print(s.getSecondLargest(arr))