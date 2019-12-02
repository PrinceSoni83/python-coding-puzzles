
# function to find out missing element in another array deraived from the first array

def find_missing_element(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1 , num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
        
    return arr1[-1]

array1 = [2,6,3,7,1,5]
array2 = [5,2,6,3,1]

print(find_missing_element(array1,array2))