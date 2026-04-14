class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = curMax = res = nums[0]

        for n in nums[1:]:
            candidates = (curMin * n, curMax * n, n)
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(curMax, res)
        
        return res
        

        


