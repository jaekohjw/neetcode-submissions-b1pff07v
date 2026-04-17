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
            if node in clones:
                return clones[node]

            new_node = Node(node.val)
            clones[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(clone(n))

            return new_node 

        return clone(node) if node else None 