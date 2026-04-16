class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visitedP = set()
        visitedA = set()

        def dfs(r, c, visited):
            if (r not in range(rows) 
                or c not in range(cols) 
                or (r, c) in visited):
                return 
            
            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows)
                    and nc in range(cols)
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        for r in range(rows):
            dfs(r, 0, visitedP)
        for c in range(cols):
            dfs(0, c, visitedP)

        for r in range(rows):
            dfs(r, cols - 1, visitedA)
        for c in range(cols):
            dfs(rows - 1, c, visitedA)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visitedP and (r, c) in visitedA:
                    res.append([r, c])
        
        return res
