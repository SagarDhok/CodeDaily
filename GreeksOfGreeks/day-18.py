# Array Subset
from collections import Counter

a= [11, 7, 1, 13, 21, 3, 7, 3] 
b= [11, 3, 7, 1, 7]

ca = Counter(a)
cb = Counter(b)

for i in b:
  if cb[i]>ca[i]:
   res = False
   break

res=  True

print("B is Subset Of A ") if res else print("B is NOT a Subset of A")