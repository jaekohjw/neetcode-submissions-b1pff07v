from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def isMatch(m, n):
            if n < 0:
                return m < 0
            if m < 0:
                return p[n] == '*' and isMatch(m, n - 2)
            
            if p[n] == "*":
                leave = isMatch(m, n - 2)
                take = p[n - 1] in {s[m], "."} and isMatch(m - 1, n)
                return leave or take 
            return p[n] in {s[m], "."} and isMatch(m - 1, n - 1)
        
        return isMatch(len(s) - 1, len(p) - 1)

        