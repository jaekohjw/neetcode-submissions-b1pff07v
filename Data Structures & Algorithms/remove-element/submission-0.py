class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

        cnt = 0 

        for num in nums:
            if num == val:
                cnt += 1 

        for i in range(len(nums)):
            if nums[i] == val:
                j = i + 1
                while j < len(nums) and nums[j] == val:
                    j += 1 
                if j < len(nums):
                    swap(nums, i, j)
                else:
                    nums[i] = 0
        
        return len(nums) - cnt
        

        