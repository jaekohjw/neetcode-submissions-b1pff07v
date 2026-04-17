class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReq = [[] for _ in range(numCourses)]
        states = [0] * numCourses

        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        def has_cycle(crs):
            if states[crs] == 1:
                return True
            if states[crs] == 2:
                return False 

            states[crs] = 1
            for pre in preReq[crs]:
                if has_cycle(pre):
                    return True 
            
            states[crs] = 2
            return False

        for crs in range(numCourses):
            if has_cycle(crs):
                return False 
        return True 



