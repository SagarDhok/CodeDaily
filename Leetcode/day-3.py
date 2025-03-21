
# With Function: Merge Two Sorted Linked Lists in Python
lst1 = []
lst2 = []
lst3 = lst2+lst1
lst3.sort()
print(lst3)

# Without Function: Efficiently Merging Two Sorted Linked Lists
list1 = [1,2,4]
list2 = [1,3,4]
lst3 = []
for i in list1:
   lst3.append(i)
for j in list2:
   lst3.append(j)
for i in range(len(lst3)):
   for j in range(i+1,len(lst3)-1):
      if lst3[i]>lst3[j]:
         lst3[i],lst3[j]=lst3[j],lst3[i]
print(lst3)