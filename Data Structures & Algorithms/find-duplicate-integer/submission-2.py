class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        