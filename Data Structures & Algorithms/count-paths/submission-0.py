from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def numPaths(i, j):
            if  i == m - 1 or j == n - 1:
                return 1
            
            return numPaths(i + 1, j) + numPaths(i, j + 1)
        
        return numPaths(0, 0)