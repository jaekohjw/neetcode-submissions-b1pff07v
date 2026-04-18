class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        uf = UnionFind(N * N)

        def get_index(r, c):
            return r * N + c

        cells = []
        for r in range(N):
            for c in range(N):
                cells.append((grid[r][c], r, c))
        cells.sort()

        submerged = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for h, r, c in cells:
            submerged.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) in submerged:
                    uf.union(get_index(r, c), get_index(nr, nc))

            if uf.find(get_index(0, 0)) == uf.find(get_index(N - 1, N - 1)):
                return h


        
        
            


    
            
        