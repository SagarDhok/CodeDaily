

class Solution:
    def toLowerCase(self, s: str) -> str:
        k=""
        for i in s: 
            if "A"<=i<="Z":
                k +=chr(ord(i)+32)
            else:
                k+=i
        return k
obj = Solution()
s = input("Enter A String : ")
print(obj.toLowerCase(s))