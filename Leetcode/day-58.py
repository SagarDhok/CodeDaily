

# Find Numbers with Even Number of Digits
# class Solution:
#     def findNumbers(self, nums):
#         length = [len(str(i)) for i in nums]

#         count = 0
#         for j in length:
#          if j%2==0:
#           count  +=1
#         return count
# s = Solution()
# print(s.findNumbers([12,345,2,6,7896]))
# print(s.findNumbers([555,901,482,1771]))

numbers = [12, 345, 2, 6, 7896]
digit_counts = [0] * len(numbers) 
for i in numbers:
   count = 0
   n= i
   while n>0:
      n = n//10
      count +=1
      digit_counts[i] = count 