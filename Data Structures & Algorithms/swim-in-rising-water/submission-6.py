class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = {(0,0)}
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

            


    
            
        