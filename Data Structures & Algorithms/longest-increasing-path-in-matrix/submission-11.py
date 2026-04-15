
import sys
sys.setrecursionlimit(15000)


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        memo = {}

        def LIP(i, j, prev):

            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            curr = matrix[i][j]
            if curr <= prev:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = 1 + max(
                LIP(i , j - 1, curr),
                LIP(i, j + 1, curr),
                LIP(i + 1, j, curr),
                LIP(i - 1, j, curr)
            )

            return memo[(i, j)]

        maxx = 0
        for i in range(m):
            for j in range(n):
                maxx = max(maxx, LIP(i, j, -1))
        
        return maxx
        