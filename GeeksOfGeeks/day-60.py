
# Segregate Even and Odd numbers
class Solution:
 def segregateEvenOdd(self,arr):

        evn =[]
        odd = []
        
        for i in arr:
          if i%2==0:
            evn.append(i)
          else:
            odd.append(i)
        
        if not evn:
          arr[:] = evn+odd
        elif not odd :
          arr[:] = evn+odd
        else:
         evn.sort()
         odd.sort()
         arr[:] = evn+odd
        
        return arr

s = Solution()
arr = [int(i) for i in input("Enter List of Number : ").split()]
print(s.segregateEvenOdd(arr))