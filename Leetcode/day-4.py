

# Find the Index of the First Occurrence in a String
haystack = input("Enter first word : ")
needle = input("Enter second word : ")
if needle in haystack :
     print(haystack.index(needle))
else:
     print(-1)
print("or")
print(haystack.find(needle))

