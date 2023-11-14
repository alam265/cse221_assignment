def dfs(grid, row, col, visited):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    
    visited[row][col] = True
    diamonds = 0
    
    if grid[row][col] == 'D':
        diamonds = 1
    
    diamonds += dfs(grid, row+1, col, visited)
    diamonds += dfs(grid, row-1, col, visited)
    diamonds += dfs(grid, row, col+1, visited)
    diamonds += dfs(grid, row, col-1, visited)
    
    return diamonds


def max_diamonds(grid,rows,cols):
    visited = [[False] * cols for _ in range(rows)]
    maximum = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                diamonds = dfs(grid, i, j, visited)
                maximum = max(maximum, diamonds)
    
    return maximum


data = open('input6.txt','r')
size = data.readline().split()
result = open('output6.txt','w')

grid = []
for i in range(int(size[0])):
    g = data.readline().strip()
    g_l = list(g)
    grid.append(g_l)


result.write(str(max_diamonds(grid,int(size[0]),int(size[1])))) 

data.close()
result.close()


'''
Explanation:
This problem is solved using DFS. In the dfs function first checked row and column is in the bound or there is a 
obstacle or it is already visited. Then we mark the path as visited and if there is a diamond diamonds variable 
is increased by 01. Them recursively call the dfs for adjacent up, down, left and right. In the max_diamonds 
function a variable is kept to keep track of the visited paths. 
'''