

def canRearrange(arr):
  arr.sort()  

  for i in range(1, len(arr), 2):
      arr[i], arr[i - 1] = arr[i - 1], arr[i]

  for i in range(1, len(arr), 2):
        if arr[i] <= arr[i - 1]:
              return False
  return True
  
arr = [5, 4, 3, 2, 1]
print(canRearrange(arr))