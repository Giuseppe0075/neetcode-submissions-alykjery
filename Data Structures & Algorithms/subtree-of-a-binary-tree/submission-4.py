# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isTheSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False
        if root.val != subRoot.val:
            return False
        return self.isTheSameTree(root.left, subRoot.left) and self.isTheSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isTheSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        