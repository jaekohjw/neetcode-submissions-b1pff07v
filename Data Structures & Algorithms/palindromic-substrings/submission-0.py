class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        cnt = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1])
                if dp[i][j]:
                    cnt += 1

        return cnt
        
        