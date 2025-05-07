
# Quick Left Rotation
def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    arr[:]= arr[k:] + arr[:k]
    return arr

print(left_rotate([1, 2, 3, 4, 5, 6, 7], 2))   
print(left_rotate([1, 2, 3, 4, 5, 6], 12))     
print(left_rotate([1, 2, 3, 4, 5, 6], 11))     

