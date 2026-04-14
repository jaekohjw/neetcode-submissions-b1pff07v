# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return (0, 0)
            l, r = helper(root.left), helper(root.right)
            h = 1 + max(l[0], r[0])
            return [h, max(l[0] + r[0], l[1], r[1])]
        return helper(root)[1]

        