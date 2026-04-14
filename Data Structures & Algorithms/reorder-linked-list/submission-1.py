# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        curr, prev = slow.next, None 
        slow.next = None

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp

        list1, list2 = head, prev

        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2 
            list2.next = tmp1
            list1, list2 = tmp1, tmp2

        


