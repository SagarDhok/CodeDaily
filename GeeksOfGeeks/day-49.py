

# Palindrome Array
#APPROACH - 1
def is_palindrome(arr):
  left = 0
  right = len(arr)-1
  while left<right:
    if arr[left]!=arr[right]:
      return False
    left +=1
    right -=1
  return True
print(is_palindrome([1, 2, 3, 2, 1])) 
print(is_palindrome([1, 2, 3, 4, 5])) 


# APPROACH - 2
arr = [1,2,3,4,5]
print(arr==arr[::-1])


