class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dummy = ListNode()

        for num in nums:
            curr = dummy
            prev = None 
            while curr:
                if curr.val == num:
                    return num 
                prev = curr
                curr = curr.next
            prev.next = ListNode(num)
            

        