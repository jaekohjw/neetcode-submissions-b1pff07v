# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        else:
            length = 0
            curr = head
            while curr:
                length = length + 1
                curr = curr.next

            if n == length:
                return head.next
            else:
                pos = length - n - 1
                curr = head 

                while pos != 0:
                    curr = curr.next 
                    pos -= 1
        
                curr.next = curr.next.next
                return head


        
        

        