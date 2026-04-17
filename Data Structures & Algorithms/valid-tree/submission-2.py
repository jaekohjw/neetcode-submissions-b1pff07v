class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]
        rank = [0] * n
        

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union_by_rank(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False 
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px 
            if rank[px] == rank[py]:
                rank[px] += 1
            return True 

        for u, v in edges:
            if not union_by_rank(u, v):
                return False 
        return True
