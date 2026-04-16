class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        maxx = 0

        def dfs(i, j):
            if i not in range(m) or j not in range(n) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + sum(dfs(i+di, j+dj) for di, dj in [(0,1),(0,-1),(-1,0),(1,0)])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxx = max(maxx, dfs(i, j))

        return maxx
                    
            

            
        