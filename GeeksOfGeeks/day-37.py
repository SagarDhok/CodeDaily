
#!Rotating an Array
class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        d = d % n  
        arr[:] = arr[d:] + arr[:d]  
arr = [1, 2, 3, 4, 5]
Solution().leftRotate(arr, 2)
print(arr)


#APPROACH - 2
arr= [-1, -2, -3, 4, 5, 6, 7]
d = 2
for i in range(d):
   arr.append(arr[0])
   arr.remove(arr[0])
   i +=1
print(arr)