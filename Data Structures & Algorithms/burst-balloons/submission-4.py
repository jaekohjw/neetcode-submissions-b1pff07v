from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]

        @cache
        def maxC(start, end):
            if start > end:
                return 0

            
            maxx = 0
            for i in range(start, end + 1):
                maxx = max(
                    maxC(start, i - 1)  
                    + nums[start - 1] * nums[i] * nums[end + 1] 
                    + maxC(i + 1, end),
                    maxx)
            return maxx
        
        return maxC(1, len(nums) - 2)

