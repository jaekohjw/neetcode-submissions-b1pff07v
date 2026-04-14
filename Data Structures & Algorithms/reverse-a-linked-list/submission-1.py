# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            reverse_next = self.reverseList(head.next)
            curr = reverse_next
            while curr.next:
                curr = curr.next
            curr.next = ListNode(head.val, None) 
            return reverse_next
                

        