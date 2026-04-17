class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = [[] for _ in range(n)]
        visited = set()
        components = 0

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            if node in visited:
                return 

            visited.add(node)

            for n in adj_list[node]:
                dfs(n)
        
        for node in range(n):
            if node not in visited:
                print(node)
                dfs(node)
                components += 1
        
        return components



