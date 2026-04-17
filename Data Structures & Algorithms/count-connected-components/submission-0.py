class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        parent = [i for i in range(n)]
        rank = [0] * n
        component = n 

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal component
            px, py = find(x), find(y)
            if px == py:
                return 

            if rank[px] < rank[py]:
                px, py = py, px
            
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1 
            component -= 1 

        for u, v in edges:
            union(u, v)
        return component
            

        