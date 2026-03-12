



class Solution:
    def floorSqrt(self, n): 
        left = 1
        right = n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == n:
                return mid

            if square < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
s = Solution()
n = int(input("Enter A Number : "))
print(s.floorSqrt(n))

