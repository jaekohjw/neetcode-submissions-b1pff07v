class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {0:[nums[0], nums[0]]}

        def helper(i):

            if i in memo:
                return memo[i]

            res = helper(i-1)
            maxBefore, minBefore = res[0], res[1]

            if nums[i] > 0:
                memo[i] = [max(nums[i], nums[i] * maxBefore), min(nums[i], nums[i] * minBefore)]
            else:
                memo[i] = [max(nums[i], nums[i] * minBefore), min(nums[i], nums[i] * maxBefore)]
            
            return memo[i]

        maxx = float('-inf')
        for i in range(len(nums)):
            maxx = max(helper(i)[0], maxx)
        return maxx
        
        

        


