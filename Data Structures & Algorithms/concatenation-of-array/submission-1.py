class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)
        for i, num in enumerate(nums):
            res[i] = nums[i]
            res[len(nums) + i] = nums[i]
        return res
        