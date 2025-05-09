

# Array insert at end
def insertAtEnd(arr,sizeOfArray,element):

    arr += [element]
    return arr

sizeOfArray = 6
arr = [1, 2, 3, 4, 5]
element = 90
print(insertAtEnd(arr,sizeOfArray,element))


sizeOfArray = 4
arr = [1, 2, 3]
element = 50
print(insertAtEnd(arr,sizeOfArray,element))