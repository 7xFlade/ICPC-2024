def max_charge(grid):
    charge = grid[0][0]
    # we can only go from one list to the next list on the same index
    i = 0
    j = 0
    while i+1 < n and j+1 < m:
        if charge + grid[i][j+1] > charge + grid[i+1][j]:
            charge += grid[i][j+1]
            j+=1
        else:
            charge += grid[i+1][j]
            i+=1
    while i+1 < n or j+1 < m:
        if i+1 < n:
            charge += grid[i+1][j]   
            i+= 1
        else:
            charge += grid[i][j+1]    
            j+=1       
    print(charge)

num = int(input())
for i in range(num):
    n_m = list(map(int, input().split()))
grid = []
n = n_m[0]
m = n_m[1]
for i in range(n_m[0]): 
    lst = list(map(int, input().split()))
    grid.append(lst)
max_charge(grid)