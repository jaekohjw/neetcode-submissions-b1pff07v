class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        max_cnt = 1
        max_elem = nums[0]
        for elem, cnt in freq.items():
            if cnt > max_cnt:
                max_elem = elem
                max_cnt = cnt
        return max_elem

        