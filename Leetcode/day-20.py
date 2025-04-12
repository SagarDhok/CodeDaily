
# Contains Duplicate
arr = [1,8,4,3,6,9,5,7,2,7,0]

count = {}
dno = []

for i in arr:
  if i not in count:
    count[i]= 1
  else:
    count[i]+=1
    
for j in count:
  if count[j]>=2:
       dno.append(j)
print(dno)