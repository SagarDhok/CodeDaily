
# Missing in Array
def  missarray(arr):
 n = len(arr)+1
 s = 0
 for i in range(1,n+1) :
    s = s+i
 
 misv = s-sum(arr)
 return misv
 

arr = [1, 2, 3, 5]
print(missarray(arr))

  