
# binary search

def binarySearch(haystack, needle):
    lo = 0
    hi = len(haystack)
    while lo < hi:
        midpoint = lo +(hi-lo)//2 # midpoint
        value = haystack[midpoint]
        print(f"midpoint: {midpoint}, value: {value}")
        if value==needle:
            return True
        elif value > needle:
            hi = midpoint
        else:
            lo = midpoint + 1
            
        
    return False
    
    
test1 = [1, 2, 4, 6, 7, 9, 12, 20, 26, 27]
test2 = [1, 3, 5, 6, 7, 9 , 11]

# print(binarySearch(test1, 12))
print(binarySearch(test2, 7))