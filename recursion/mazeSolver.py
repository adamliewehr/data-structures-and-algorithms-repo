dir = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
    
]


def walk(maze, wall, curr, end, seen, path): # returns a bool 
    # we want the base cases to know where we are currently
    # 1. off the map
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze): # the maze is a square
        return False
    
    # 2. on a wall
    if maze[curr.y][curr.x] == wall:
        return False
    
    # 3. are we at the end?
    if curr.x == end.x and curr.y == end.y:
        path.append(end)
        return True
    
    # 4. have we seen it?
    # seen is a 2d boolean array
    if seen[curr.y][curr.x]:
        return False

    # the recursive case is what actually moves us around
    # pre - the path argument is an array of points
        # ever time we successfully visit a spot, we will add it to the path
        # and remove it in the post condition
        
    seen[curr.y][curr.x] = True
        
    path.append(curr)

    # recurse
    
    for i in range(len(dir)): # for every direction
        x, y = dir[i]
        if walk(maze, wall, 
             {x: curr.x + x,
              y: curr.y + y}, 
             end, seen, path):
            return True
    
    # post
    path.pop()
    
    return False # if we recurse and we reach the end, and we didn't find end, its false
    
    

def solve(maze, wall, start, end): # will return a list of points from the start to the end
    
    seen = []
    path = []
    
    for i in range(len(maze)):
        seen.append([False for j in range(len(maze[0]))])

    walk(maze, wall, start, end, seen, path)
    
    return path
        
    
