
# Permutation Sequence
def getPermutation(n, k):
    import math

    digits = list(range(1, n+1))
    k -= 1  
    result = []

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        k %= fact
        result.append(str(digits.pop(index)))

    return "".join(result)

print(getPermutation(3, 3)) 
print(getPermutation(4, 9)) 
print(getPermutation(3, 1))  
