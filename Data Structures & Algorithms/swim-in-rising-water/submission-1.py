class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def dfs(r, c, t, visited):
            if r == N -1 and c == N - 1:
                return True 
            
            visited.add((r, c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    if grid[nr][nc] <= t:
                        if dfs(nr, nc, t, visited):
                            return True 
            
            return False

        max_h = max(max(row) for row in grid)

        lo = max(grid[0][0], grid[N - 1][N - 1])
        hi = max_h
        
        while lo < hi:
            visited = set()
            mid = (lo + hi) // 2
            if dfs(0, 0, mid, visited):
                hi = mid
            else:
                lo = mid + 1
            
        return lo

            
        