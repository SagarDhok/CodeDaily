

# Missing And Repeating

def findMissingAndRepeating(arr):
    n = len(arr)
    sum_expected = n * (n + 1) // 2
    sum_square_expected = n * (n + 1) * (2 * n + 1) // 6
    sum_actual = 0
    sum_square_actual = 0
    for num in arr:
        sum_actual += num
        sum_square_actual += num * num
    diff = sum_expected - sum_actual
    square_diff = sum_square_expected - sum_square_actual
    sum_ab = square_diff // diff
    a = (diff + sum_ab) // 2
    b = a - diff
    return [b, a]

print(findMissingAndRepeating([2, 2]))
print(findMissingAndRepeating([1, 3, 3]))
print(findMissingAndRepeating([4, 3, 6, 2, 1, 1]))
