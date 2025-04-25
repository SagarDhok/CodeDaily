
# Count the Occurrences: Finding Target Frequency in a Sorted Array"
def countFreq():
 arr = [1, 1, 2, 2, 2, 2, 3]
 target = 2
 count = 0
 for i in arr:
  if i == target:
   count +=1
 print("The Count Of Number Is : ",count)
countFreq()