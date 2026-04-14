# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0 
        while (l1 or l2):
            if l1 is None: 
                sum = l2.val + carry
                l2 = l2.next
            elif l2 is None: 
                sum = l1.val + carry 
                l1 = l1.next
            else:    
                sum = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next

            if sum < 10:
                carry = 0
                curr.next = ListNode(sum)
                curr = curr.next
            else:
                digit = sum % 10 
                carry = sum // 10 
                curr.next = ListNode(digit)
                curr = curr.next 

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next