# Immediate Smaller Element
def immediateSmaller(arr):
    for i in range(len(arr) - 1):  
        arr[i] = arr[i + 1] if arr[i + 1] < arr[i] else -1
    arr[-1] = -1  
    return arr

print(immediateSmaller([4, 2, 1, 5, 3]))
