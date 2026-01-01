def bubbleSort(nums):
    for i in range(len(nums), 0, -1):
        # print("pass", i)
        for j in range(0, i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                
    return nums
            
            
test1 = [1, 2, 3, 4, 5, 6]
test2 = [6, 5, 4, 3, 2, 1]
test3 = [4, 3, 5, 2, 6, 1]

print(bubbleSort(test1))
print(bubbleSort(test2))
print(bubbleSort(test2))
        
        
# ages = {"Adam": 22, "Saima": 23, "Tori": 19, "Dave": 68, "Carolyn": 29}

# items = ages.items()

# for name, age in items:
#     print(name, age)
    
# keys = ages.keys()
    
# for key in keys:
#     print(key)
    
# values = ages.values()

# for value in values:
#     print(value)