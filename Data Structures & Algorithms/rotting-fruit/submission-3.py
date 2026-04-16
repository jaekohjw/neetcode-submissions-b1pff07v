from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        cnt = 0

        while q:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            if len(q) > 0:
                cnt += 1
            

            

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return cnt
