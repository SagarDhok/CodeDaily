




class Solution:
   def common_digits(self, nums):
        st =set()
        for i in nums:
         n = i
         while n>0:
           d = n%10
           if d not in st:
             st.add(d)
           n=n//10
        return sorted(st)
		   
s = Solution()
nums = [131, 11, 48]
print(s.common_digits(nums))

nums =[111, 222, 333, 4444, 666]
print(s.common_digits(nums))