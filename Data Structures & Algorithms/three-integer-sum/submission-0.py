class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        i = 0

        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in ret:
                            ret.append(sorted([nums[i], nums[j], nums[k]]));
                    k += 1
                j += 1 
            i += 1
        
        return ret

