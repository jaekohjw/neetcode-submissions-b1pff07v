class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fprod = [0] * n
        bprod = [0] * n
        output = [0] * n

        for i in range(n):
            fprod[i] = nums[0] if i == 0 else nums[i] * fprod[i - 1]
            bprod[i] = nums[n - 1] if i == 0 else nums[n - 1 - i] * bprod[i - 1]

        for i in range(n):
            if i == 0:
                output[i] = bprod[n - 2]
            elif i == n - 1:
                output[i] = fprod[n - 2]
            else:
                output[i] = fprod[i - 1] * bprod[n - i - 2]
        return output

        
    