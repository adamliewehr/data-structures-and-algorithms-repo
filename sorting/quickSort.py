

def qs(arr, lo, hi): # returns nothing
    
    if lo >= hi:
        return
    
    pivotIdx = partition(arr, lo, hi)
    qs(arr, lo, pivotIdx-1) # recursive!
    qs(arr, pivotIdx+1, hi)
    
    # we are repeating the quick sort on the left side of the array
    # then the right side of the array
    # but we are NOT INCLUDING THE PIVOT
    

def partition(arr, lo, hi): # returns the pivot index
    pivot = arr[hi]
    
    idx = lo - 1
    # now walk from the lo to the high
    # do a weak sort on the subarray
    
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx+=1
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp
            
    idx +=1 # increment once more 
    # if we found nothing less than us, we would put pivot into the lo position
    
    arr[hi] = arr[idx]
    arr[idx] = pivot
    
    return idx
    
def quickSort(arr):
    qs(arr, 0, len(arr)-1)
    return arr


test1 = [8, 3, 15, 2, 9, 1, 7, 12]
test2 = [42, 17, 23, 17, 5, 99, 1, 64, 23]
test3 = [-3, 14, -7, 0, 8, -1, 5, -10]
test4 = [100, 90, 95, 85, 80, 110, 105]
test5 = [6, 2, 9, 4, 7, 3, 8, 1, 5]

print(quickSort(test1))
print(quickSort(test2))
print(quickSort(test3))
print(quickSort(test4))
print(quickSort(test5))