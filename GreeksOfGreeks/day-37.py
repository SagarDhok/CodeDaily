
arr= arr = [int(i) for i in input("Enter List Of Values : ").split()]
d = int(input("Enter A Number : "))
d = d % len(arr)
arr[:]  = arr[d:]+arr[:d]
print(arr[:])



