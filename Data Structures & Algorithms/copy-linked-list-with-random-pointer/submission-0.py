"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0, None, None)
        curr2 = dummy
        nodes = {}

        curr = head
        while curr:
            curr2.next = Node(curr.val, None, None)
            nodes[curr] = curr2.next
            curr = curr.next
            curr2 = curr2.next


        curr = head
        curr2 = dummy.next
        while curr:
            if curr.random:
                curr2.random = nodes[curr.random]
            curr = curr.next
            curr2 = curr2.next
        
        return dummy.next
            