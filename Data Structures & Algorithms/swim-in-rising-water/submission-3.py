from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def bfs(t):
            
            q = deque([(0, 0)])
            visited = set([(0, 0)])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while q:
                r, c = q.popleft()

                if r == N - 1 and c == N - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                        if grid[nr][nc] <= t:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            
            return False 

        max_h = max(max(row) for row in grid)

        lo = max(grid[0][0], grid[N - 1][N - 1])
        hi = max_h
        
        while lo < hi:
            mid = (lo + hi) // 2
            if bfs(mid):
                hi = mid
            else:
                lo = mid + 1
            
        return lo

            
        