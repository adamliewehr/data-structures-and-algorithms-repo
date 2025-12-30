# two crystal balls problem
# implementation

# creating a random array of 0s, and then to 1s
# how can we do this
# well is it possible for the ball to never break?
# meaning the ball will survive the n story drop
# let's say yes for fun
# well we can get a random number from 1-n
# and populate a list with that number of 0s

import random
# we are going to do 100 just to keep it simple
numOfZeros = random.randint(0, 100) # inclusive on both sides
floors = [0] * numOfZeros

# then we fill the rest of the list with 1s
ones = [1] * (100-numOfZeros)

floors = floors+ones

# just to check:
# print(floors)
# print(len(floors))

# great! now we have our random input array
# the answer should be the number of 0s + 1, so lets do that now

ans = numOfZeros

# now let's implement the algo

print(floors)

def squirtSearch(arr):
    increment = int(len(arr)**(1/2)) # getting the sqrt() without importing math
    lastPoint = 0
    for i in range(0, len(arr), increment):
        if i > 1 and arr[i] == 1 and arr[i-1]==0:
            return i
        if arr[i] == 1: # we found where the point at which the ball will break, now we backtrack
            break
        lastPoint = i
    for j in range(lastPoint, lastPoint+increment):
        if arr[j]==1:
            return j
    return -1
        
print("ans:", ans)
print("from function:", squirtSearch(floors)) 