class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = - nums[i]

            l, r = i + 1, len(nums) - 1

            while l < r: 
                if nums[l] + nums[r] == target:
                    ret.append([nums[i], nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                if nums[l] + nums[r] < target:
                    l += 1
                else: 
                    r -= 1   
        return ret

