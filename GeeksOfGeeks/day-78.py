

# Kth Smallest

def kthSmallest(arr,k):
        
        
            import random
        
            def partition(left, right, pivot_index):
                pivot = arr[pivot_index]
                arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
                store_index = left
                for i in range(left, right):
                    if arr[i] < pivot:
                        arr[store_index], arr[i] = arr[i], arr[store_index]
                        store_index += 1
                arr[right], arr[store_index] = arr[store_index], arr[right]
                return store_index
        
            def select(left, right, k_smallest):
                if left == right:
                    return arr[left]
                pivot_index = random.randint(left, right)
                pivot_index = partition(left, right, pivot_index)
                if k_smallest == pivot_index:
                    return arr[k_smallest]
                elif k_smallest < pivot_index:
                    return select(left, pivot_index - 1, k_smallest)
                else:
                    return select(pivot_index + 1, right, k_smallest)
        
            return select(0, len(arr) - 1, k - 1)
      




arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print(kthSmallest(arr1, k1))

arr2 = [2, 3, 1, 20, 15]
k2 = 4
print(kthSmallest(arr2, k2))