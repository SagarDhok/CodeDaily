


# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter" ]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

res  = {}
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            res[list1[i]]= i+j

minv = min(res.values())


for val in res:
    if res[val]==minv:
        print(val)