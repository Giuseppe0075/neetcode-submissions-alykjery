# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDepth(self, root, d):
        if not root:
            return 0
        return max(self.findDepth(root.left, d), self.findDepth(root.right, d)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findDepth(root, 0)