# # starting simple
# # linear search through an array

def search(arr, v): # takes in an array, and a value v
    for value in arr:
        if value==v:
            return True
    return False

arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [1, 2, 3, 4, 5, 7, 8]

print(search(arr1, 6))
print(search(arr2, 6))

# big O is O(n)
