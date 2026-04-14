from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def numWays(i):
            if i <= 1:
                return 1
            else:
                return numWays(i - 1) + numWays(i - 2)
    
        return numWays(n)

        
