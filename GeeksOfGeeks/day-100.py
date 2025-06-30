
#! Maximum triplet sum in array

class Solution:
    def maxTripletSum(self, arr) : 
        first = second = third = float('-inf')
    
        for num in arr:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        return first + second + third
s = Solution()
print(s.maxTripletSum([int(i) for i in input("Enter Array Elements : ").split()]))