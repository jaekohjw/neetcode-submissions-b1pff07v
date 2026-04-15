import sys
sys.setrecursionlimit(15000)

from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        @cache
        def LIP(i, j):

            curr = matrix[i][j] 
            res = 1

            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > curr:
                    res = max(res, 1 + LIP(ni, nj))

            return res

        maxx = 0
        for i in range(m):
            for j in range(n):
                maxx = max(maxx, LIP(i, j))
        
        return maxx
        