
#! Check if a given number is a power of two
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

n = int(input("Enter a number: "))

if isPowerOfTwo(n):
    print(f"{n} is a power of 2")
else:
    print(f"{n} is not a power of 2.")
