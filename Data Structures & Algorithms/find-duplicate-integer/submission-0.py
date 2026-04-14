class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return sorted_nums[i]

        