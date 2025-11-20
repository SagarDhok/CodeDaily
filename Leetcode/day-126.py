
#! 989. Add to Array-Form of Integer
class Solution:
    def addToArrayForm(self, num, k):
        i = len(num) - 1
        carry = k
        res = []

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1

            res.append(carry % 10)
            carry //= 10

        return res[::-1]


s = Solution()
num = [1,2,0,0]
k = 34
print(s.addToArrayForm(num,k))

num = [2,7,4]
k = 181
print(s.addToArrayForm(num,k))

num = [2,1,5]
k = 806
print(s.addToArrayForm(num,k))