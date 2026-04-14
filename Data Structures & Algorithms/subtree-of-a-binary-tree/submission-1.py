# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False


        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 is None or root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
                
        
        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        