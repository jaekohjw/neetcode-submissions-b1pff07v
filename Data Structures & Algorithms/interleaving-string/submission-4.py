from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        @cache
        def dfs(i, j):
            # Base case: If we successfully consumed both strings
            if i == len(s1) and j == len(s2):
                return True
            
            # Check if we can pull the next character from s1
            # (i < len(s1) ensures we don't get an index out of bounds error)
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
                
            # Check if we can pull the next character from s2
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
                
            return False
            
        return dfs(0, 0)



        