class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        summ //= 2
        
        dp = [[-1] * (summ + 1) for i in range(len(nums))]
        def canGet(i, target):
            if i < 0:
                return False
            if target == 0:
                return True
            if dp[i][target] != -1:
                return dp[i][target]
            
            
            dp[i][target] = canGet(i - 1, target)
            if dp[i][target]:
                return dp[i][target]

            if nums[i] <= target:  
                dp[i][target] = canGet(i - 1, target - nums[i])
            return dp[i][target]
        
        return canGet(len(nums) - 1, summ)
