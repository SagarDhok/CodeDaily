

# Minimum Jumps
def minJumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    maxReach = arr[0]
    step = arr[0]
    jump = 1
    for i in range(1, n):
        if i == n - 1:
            return jump
        maxReach = max(maxReach, i + arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= maxReach:
                return -1
            step = maxReach - i
    return -1

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(minJumps([1, 4, 3, 2, 6, 7]))
print(minJumps([0, 10, 20]))
print(minJumps([1, 1, 1, 1, 1]))
print(minJumps([2, 3, 1, 1, 4]))
print(minJumps([1, 0, 1, 0]))
print(minJumps([5, 4, 3, 2, 1, 0, 0]))
print(minJumps([3, 2, 1, 0, 4]))
print(minJumps([1]))
print(minJumps([2, 0, 2, 0, 1]))
