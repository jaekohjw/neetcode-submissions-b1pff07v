class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):

        house0, house1 = 0, 0 
        for rob in nums:
            house0, house1 = house1, max(house0 + rob, house1)
        return house1

        

        
    

        