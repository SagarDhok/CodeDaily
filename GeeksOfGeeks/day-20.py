# Print 1 To N Without Loop

class Solution():
 def printNos(self,n):
       if n == 0:
         return 
       self.printNos(n-1)
       print(n,end=" ")

o = Solution()
n = int(input("Enter A Number : "))
o.printNos(n)


#or 

def printNos(i,n):
              if i>n:
                      return
              else:
                      print(i,end = " ")
                      printNos(i+1,n)
n = int(input("Enter A Number : "))
printNos(1,n)