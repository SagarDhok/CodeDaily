


# Strongest Neighbour
def maximumAdjacent(arr):
    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
              print(arr[i], end=" ") 
        else:
              print(arr[i + 1], end=" ") 
            

print(maximumAdjacent([1,2,2,3,4,5]))
print(maximumAdjacent([5,5]))


