
def fun(arr):
 
 for i in range(len(arr)):
  if arr[i] == 1:
   return i
  
 return -1
  
arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
print(fun(arr))