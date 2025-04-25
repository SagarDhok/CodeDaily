
# Rotate Array by One

arr=  [1, 2, 3, 4, 5]  #op [5, 1, 2, 3, 4]
arr.insert(0,arr[-1])
arr.pop(-1)
print(arr)     

#or

arr=  [1, 2, 3, 4, 5] 
arr.insert(0,arr.pop())
print(arr)     

#or

arr = [arr[-1]] + arr[:-1]
print(arr)