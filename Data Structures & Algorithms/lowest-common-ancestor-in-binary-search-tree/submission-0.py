# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        rval = root.val
        pval = p.val
        qval = q.val 

        if pval < rval and qval < rval:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pval > rval and qval > rval:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        