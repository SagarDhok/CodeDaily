

# Convert a Number to Hexadecimal
class Solution:
    def toHex(self, num: int) -> str:
            return hex(num & 0xFFFFFFFF)[2:]
s = Solution()
num = int(input("Enter A Number : "))
print(s.toHex(num))