# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0 
        while (l1 or l2 or carry):
            v1 = 0 if l1 is None else l1.val 
            v2 = 0 if l2 is None else l2.val

            sum = v1 + v2 + carry
            if sum < 10:
                carry = 0
                curr.next = ListNode(sum)
            else:
                digit = sum % 10 
                carry = sum // 10 
                curr.next = ListNode(digit)

            curr = curr.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            


        return dummy.next