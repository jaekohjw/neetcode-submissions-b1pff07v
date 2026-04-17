from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            in_degree[crs] += 1
            adj_list[pre].append(crs)

        
        
        numFinished = 0
        q = deque([crs for crs in range(numCourses) if in_degree[crs] == 0])

        while q:
            crs = q.popleft()
            numFinished += 1 
            for n in adj_list[crs]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)

        return numFinished == numCourses