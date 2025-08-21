

#! Face off Tournament
def winner(arr, m, n):
    count_m = 0
    count_n = 0
    for i in arr:
        if i%m==0:
            count_m+=1
            
        if i%n==0:
            count_n+=1
    
    if count_m>count_n:
        return "Ram"
    elif count_n>count_m:
        return "Rohan"
    else:
        return "Both"
    
arr = [4, 5, 7, 6, 9, 10, 14]
m = 2
n = 3
print(winner(arr,m,n))

arr = [1, 9, 9, 10, 9, 18]
m = 5
n = 3
print(winner(arr,m,n))