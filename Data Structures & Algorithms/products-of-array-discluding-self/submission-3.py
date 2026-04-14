class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        prod = 1

        for num in nums:
            if num == 0:
                numZeros += 1
            else:
                prod = prod * num
        
        if numZeros > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if numZeros: res[i] = 0 if num else prod
            else: res[i] = prod // num
        return res

    