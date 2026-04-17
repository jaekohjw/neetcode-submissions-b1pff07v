class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(node, parent):
 
            if node in visited:
                return False 

            visited.add(node)

            for n in adj_list[node]:
                if n == parent:
                    continue 
                if not dfs(n, node):
                    return False
            
            return True 

        return dfs(0, -1) and len(visited) == n
                
