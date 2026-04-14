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
        elif numZeros == 1:
            output = []
            for i in range(len(nums)):
                output.append(prod if nums[i] == 0 else 0)
            return output
        else:
            output = []
            for i in range(len(nums)):
                output.append(prod // nums[i])
            return output

    