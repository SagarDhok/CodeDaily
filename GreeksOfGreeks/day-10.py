
# Find the First Occurrence of a Substring
txt = input("Enter A Word : ")
pat = input("Enter A Word That you Want to Check  : ")
if pat in txt : 
     print(txt.index(pat))
else:
     print(-1)