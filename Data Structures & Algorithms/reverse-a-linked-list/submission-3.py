# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        else:
            reverse = self.reverseList(head.next)
            if not reverse:
                return head
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = head
            head.next = None
            return reverse
            