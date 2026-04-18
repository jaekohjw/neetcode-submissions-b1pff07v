class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c, t):
            if r not in range(rows) or c not in range(cols):
                return False 
            
            if grid[r][c] > t:
                return False
            
            if r == rows - 1 and c == cols - 1:
                return True 

            visited.add((r, c))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                    if dfs(nr, nc, t):
                        return True 
            
            return False

        max_h = 0
        for r in range(rows):
            for c in range(cols):
                max_h = max(max_h, grid[r][c])

        lo = max(grid[0][0], grid[rows - 1][cols - 1])
        hi = max_h
        
        while lo < hi:
            visited = set()
            mid = (hi - lo) // 2 + lo
            if dfs(0, 0, mid):
                hi = mid
            else:
                lo = mid + 1
            
        return lo

            
        