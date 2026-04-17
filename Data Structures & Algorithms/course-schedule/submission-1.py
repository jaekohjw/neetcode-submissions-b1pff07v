class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        stack = []
        adj_lst = {}

        for u, v in prerequisites:
            adj_lst.setdefault(v, []).append(u)

        def dfs(node):
            visited.add(node)
            stack.append(node)

            for n in adj_lst.get(node, []):
                if n not in visited:
                    if dfs(n):
                        return True 
                elif n in stack:
                    return True 
            
            stack.pop()
            return False

        for u in range(numCourses):
            if u not in visited:
                if dfs(u):
                    return False 
        return True



        



        