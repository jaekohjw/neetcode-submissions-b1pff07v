class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def maxI(i):
            if i < 0: 
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(maxI(i - 2) + nums[i], maxI(i - 1))
            return dp[i]
        return maxI(len(nums) - 1)