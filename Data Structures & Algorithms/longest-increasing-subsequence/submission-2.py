
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        n = len(nums)
        dp = [-1] * n
        dp[0] = 1

        for i in range(1, n):
            maxx = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxx = max(dp[j], maxx)
            dp[i] = maxx + 1
        
        maxx = 0
        for i in range(n):
            maxx = max(dp[i], maxx)
        return maxx
        