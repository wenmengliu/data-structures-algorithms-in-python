class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # finid the start point position and count how many non-obstacle squares that we need to walk over
        # n = 1 includes the start point
        sx, sy, n = -1, -1, 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    n += 1
        return self.dfs(sx, sy, n, grid)
    
    def dfs(self, x, y, n, grid):
        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == -1:
            return 0
        if grid[x][y] == 2:
            # to see if we go over all of non-obstacle squares
            return n == 0

        # mark the current position as obstacle
        grid[x][y] = -1

        paths = self.dfs(x, y+1, n-1, grid) + self.dfs(x, y-1, n-1, grid) + self.dfs(x - 1, y, n-1, grid) + self.dfs(x+1, y, n-1, grid)

        # backtracking
        grid[x][y] = 0

        return paths