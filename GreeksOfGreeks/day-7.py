# Check if a Number is Prime
def CheckPrime(n):
 if n<=1:
      return False
         
 for i in range(2,n):
      if n%i == 0:
       return False
            
 return True
n = int(input("Enter A Number To check Whether It is Prime Or not : "))
res = CheckPrime(n)
print(f"{n} Is Prime Number : {res}")