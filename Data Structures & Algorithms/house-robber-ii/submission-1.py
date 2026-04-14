class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        def maxAmt(i, current_nums, dp):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = max(maxAmt(i - 1, current_nums, dp),
                            maxAmt(i - 2, current_nums, dp) + current_nums[i])
                return dp[i]

        list1 = nums[:-1]
        dp1 = [-1] * len(list1)
        
        list2 = nums[1:]
        dp2 = [-1] * len(list2)

        return max(maxAmt(len(list1) - 1, list1, dp1), 
                   maxAmt(len(list2) - 1, list2, dp2))