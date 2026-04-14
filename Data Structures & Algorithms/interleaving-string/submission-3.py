from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l = len(s1) 
        m = len(s2)
        n = len(s3)

        if l + m != n:
            return False 
        
        @cache
        def canIL(i, j, k):
            if k == n:
                return True
            c1 = s1[i] if i < l else None
            c2 = s2[j] if j < m else None
            if s3[k] != c1 and s3[k] != c2:
                return False 
            if c1 and s3[k] == s1[i]:
                if  c2 and s3[k] == s2[j]:
                    return canIL(i + 1, j, k + 1) or canIL(i, j + 1, k + 1)
                return canIL(i + 1, j, k + 1)

            if c2 and s3[k] == s2[j]:
                return canIL(i, j + 1, k + 1)
        
        return canIL(0, 0, 0)

        