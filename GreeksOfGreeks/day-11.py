# Sum of first n terms

n = int(input("Enter A number : "))
sum = 0
for i in range(1,n+1):
     sum = sum+i**3
print(sum)