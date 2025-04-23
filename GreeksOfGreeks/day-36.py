
# Binary Array Sorting
def binSort(arr):
    zero_count = arr.count(0)
    for i in range(len(arr)):
        if i < zero_count:
            arr[i] = 0
        else:
            arr[i] = 1
    print(arr)

binSort([1, 0, 1, 1, 0])


def binSort(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1

    print(arr)

binSort([1, 0, 1, 1, 0])



def binSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)

binSort([1, 0, 1, 1, 0])
