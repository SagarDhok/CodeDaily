

# Reverse array in groups

def reverseInGroups(arr,k):
        for i in range(0,len(arr),k):
           group = arr[i:i+k][::-1]
           arr[i:i+k] = group
        return arr


arr = [int(i) for i in input("Enter List of Values : ").split()]
k = int(input("Enter a number: "))
print(reverseInGroups(arr,k))



