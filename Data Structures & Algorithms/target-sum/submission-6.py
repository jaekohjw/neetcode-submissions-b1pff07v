from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def numWays(i, target):
            if i < 0:
                return 0
            if i == 0:
                if abs(nums[i]) == abs(target):
                    return 2 if nums[i] == 0 else 1
                return 0
            return numWays(i - 1, target + nums[i]) + numWays(i - 1, target - nums[i])

        return numWays(len(nums) - 1, target)
        