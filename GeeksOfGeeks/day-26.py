
# Count the Digits That Divide
def evenlyDivides(n):
        temp = n
        count = 0
        while n>0:
            d = n%10
            if d!=0 and temp%d==0 :
                count +=1
            n = n//10
        return count
n = int(input("Enter A Number : "))
print(evenlyDivides(n))