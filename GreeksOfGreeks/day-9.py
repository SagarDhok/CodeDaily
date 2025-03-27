
# Min and Max in Array
arr = [int(i) for i in input("Enter List of Values : ").split()]
maxv = -99999
minv = 99999
for i in arr:
          if i>maxv:
              maxv = i
for j in arr:
          if j <minv:
              minv = j
              
print(f"Max : {maxv} , Min : {minv}")