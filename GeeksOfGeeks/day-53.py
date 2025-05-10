
# Find the fine

class Solution:
  def totalFine(self, date, car, fine):
 
   total_fine = 0
   for i in range(len(car)):
      if date%2==0:
         if car[i]%2!=0:
            total_fine+=fine[i]
      else:
          if car[i]%2==0:
           total_fine+=fine[i]
   return total_fine 
 
 
date = 12
car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]
s = Solution()
print(s.totalFine(date,car,fine))

date = 8
car = [2222, 2223, 2224]
fine = [200, 300, 400]
s = Solution()
print(s.totalFine(date,car,fine))