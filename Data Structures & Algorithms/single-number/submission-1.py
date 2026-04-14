class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            ret = ret ^ nums[i]
        return ret
        