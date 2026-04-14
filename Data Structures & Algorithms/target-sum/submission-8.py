from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def numWays(i, target):
            if i < 0:
                return 1 if target == 0 else 0
   
            return numWays(i - 1, target + nums[i]) + numWays(i - 1, target - nums[i])

        return numWays(len(nums) - 1, target)
        