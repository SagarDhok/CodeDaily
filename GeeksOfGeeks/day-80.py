

# Longest Subarray with Sum K
def longest_subarray_with_sum_k(a, k):
    s = 0
    m = 0
    d = {}
    for i, x in enumerate(a):
        s += x
        if s == k:
            m = i + 1
        if s - k in d:
            m = max(m, i - d[s - k])
        if s not in d:
            d[s] = i
    return m
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))    
print(longest_subarray_with_sum_k([-5, 8, -14, 2, 4, 12], -5))    
print(longest_subarray_with_sum_k([10, -10, 20, 30], 5))          
