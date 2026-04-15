from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def isMatch(m, n):
            if m < 0:
                return n < 0 or (n == 1 and p[n] == "*")
            if n < 0:
                return False
            
            if p[n] == ".":
                return isMatch(m - 1, n - 1)
            if p[n] == "*":
                preChar = p[n - 1]
                idx = m 
                while idx >= 0 and (preChar == "." or s[idx] == preChar):
                    if isMatch(idx, n - 1):
                        return True
                    idx -= 1
                return isMatch(m, n - 2)
            return s[m] == p[n] and isMatch(m - 1, n - 1)
        
        return isMatch (len(s) - 1, len(p) - 1)

        