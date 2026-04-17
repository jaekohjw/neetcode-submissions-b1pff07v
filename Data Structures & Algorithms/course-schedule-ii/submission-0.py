from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        order = []
        num_finished = 0

        for crs, pre in prerequisites:
            in_degree[crs] += 1
            adj_list[pre].append(crs)

        q = deque([crs for crs in range(numCourses) if in_degree[crs] == 0])

        while q:
            crs = q.popleft()
            num_finished += 1
            order.append(crs)
            
            for n in adj_list[crs]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)

        return order if num_finished == numCourses else []

        
