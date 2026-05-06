

arr = [10, 3, 5, 6, 2]

result = [1]*len(arr)
print(result)

prefix = 1
for i in range(len(arr)):
                result[i] = prefix
                prefix = prefix*arr[i]
                