class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        max_cnt = 1
        max_elem = nums[0]
        for elem, cnt in freq.items():
            if cnt > max_cnt:
                max_elem = elem
                max_cnt = cnt
        return max_elem

        