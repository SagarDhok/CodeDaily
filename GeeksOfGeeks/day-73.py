

# Indexes of Subarray Sum
def subarray_sum(arr, target):
    n = len(arr)
    start = 0
    current_sum = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == target:
            return [start + 1, end + 1]  
    
    return [-1]

print(subarray_sum([1, 2, 3, 7, 5], 12))
print(subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))  
print(subarray_sum([5, 3, 4], 2))  
