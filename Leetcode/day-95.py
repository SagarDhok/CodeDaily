


#! 717. 1-bit and 2-bit Characters
class Solution:
        def isOneBitCharacter(self,bits):
            i = 0
            while i < len(bits) - 1:  
                if bits[i] == 1:
                    i += 2  
                else:
                    i += 1  
            return i == len(bits) - 1
s = Solution()
print(s.isOneBitCharacter([int(i) for i in input("Enter Array Elements : ").split()]))