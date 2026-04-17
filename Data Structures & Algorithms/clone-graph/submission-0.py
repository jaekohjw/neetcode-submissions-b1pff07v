"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        clones = {}
        def clone(node):
            if not node:
                return node
            if not node.neighbors:
                new_node = Node(node.val)
                return new_node
            if node in clones:
                return clones[node]

            new_node = Node(node.val)
            clones[node] = new_node
            new_node.neighbors = [clone(n) for n in node.neighbors]
            
            return new_node
        
        return clone(node)