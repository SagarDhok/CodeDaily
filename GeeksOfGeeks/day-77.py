

# Game with nos

def game_with_number (arr,  n) : 
    for i in range(n - 1):
        arr[i] = arr[i] ^ arr[i + 1]
    return arr

arr= [10, 11, 1, 2, 3]
n = 4
print(game_with_number(arr, n))


arr = [5, 9, 7, 6]
n = 4
print(game_with_number(arr, n))
