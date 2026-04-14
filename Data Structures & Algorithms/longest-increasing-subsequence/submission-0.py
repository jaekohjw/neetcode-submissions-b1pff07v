
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        dp = [-1] * len(nums)

        def LIS(i):
            if dp[i] != -1:
                return dp[i]

            maxx = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxx = max(maxx, LIS(j))
            dp[i] = maxx + 1
            return dp[i]

        maxL = 1
        for i in range(len(nums)):
            maxL = max(maxL, LIS(i))
        return maxL
        