# Count Odd and Even
arr = [1, 2, 3, 4, 5]
ec = 0
oc = 0
for i in arr:
	if i%2 == 0:
		ec = ec+1
	elif i%2!=0:
		oc = oc+1
print("Even Count :  ",ec)
print("Odd Count :  ",oc)