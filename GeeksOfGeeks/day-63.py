

# Count number of elements between two given elements in array
def count_elements_between(arr, num1, num2):
        left_index = -1
        right_index = -1
    
        for i in range(len(arr)):
            if arr[i] == num1:
                left_index = i
                break
    
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == num2:
                right_index = i
                break
        if left_index != -1 and right_index != -1 and right_index > left_index:
         return right_index - left_index - 1
        else:
            return 0
arr1 = [4, 2, 1, 10, 6]
num1_1 = 4
num2_1 = 6
print(f"Count between {num1_1} and {num2_1}: {count_elements_between(arr1, num1_1, num2_1)}")

arr2 = [3, 2, 1, 4]
num1_2 = 2
num2_2 = 4
print(f"Count between {num1_2} and {num2_2}: {count_elements_between(arr2, num1_2, num2_2)}")

arr3 = [3, 7, 6, 7, 1, 8, 8, 1, 8]
num1_3 = 7
num2_3 = 7
print(f"Count between {num1_3} and {num2_3}: {count_elements_between(arr3, num1_3, num2_3)}")

arr4 = [1, 2, 3, 2, 4, 5, 4]
num1_4 = 2
num2_4 = 4
print(f"Count between {num1_4} and {num2_4}: {count_elements_between(arr4, num1_4, num2_4)}")

arr5 = [5, 6, 7, 8]
num1_5 = 1
num2_5 = 9
print(f"Count between {num1_5} and {num2_5}: {count_elements_between(arr5, num1_5, num2_5)}")