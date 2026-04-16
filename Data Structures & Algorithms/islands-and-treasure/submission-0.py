from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
  
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))


        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows)
                        and nc in range(cols) 
                        and grid[nr][nc] > 0 
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
            
            

        

        