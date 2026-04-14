# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isBalancedHelper(root)[1]

    def isBalancedHelper(self, root: Optional[TreeNode]) -> (int, bool):
        if root is None:
            return (-1, True)
        else:
            lheight, lbalanced = self.isBalancedHelper(root.left)
            rheight, rbalanced = self.isBalancedHelper(root.right)
            return (1 + max(lheight, rheight), abs(lheight - rheight) <= 1 and lbalanced and rbalanced)
        