class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        states = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj_list[pre].append(crs)

        order = []

        def has_cycle(crs):
            if states[crs] == 2:
                return False
            if states[crs] == 1:
                return True 

            states[crs] = 1
            for n in adj_list[crs]:
                if has_cycle(n):
                    return True 
            
            order.append(crs)
            states[crs] = 2
            return False 

        for crs in range(numCourses):
            if states[crs] == 0 and has_cycle(crs):
                return []
        
        return order[::-1]

        