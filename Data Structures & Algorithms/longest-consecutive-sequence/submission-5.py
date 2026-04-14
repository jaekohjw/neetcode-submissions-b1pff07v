class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            dict1[num] = num
        
        max_size = 0
        for num in dict1:
            size = 1
            if (num - 1) not in dict1:
                while (num + size) in dict1:
                    size += 1
                max_size = max(size, max_size)
        
        return max_size
        