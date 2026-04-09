# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, m):
            if not root:
                return 0
            ans = 0
            if root.val >= m:
                m = root.val
                ans += 1
            return ans + solve(root.left, m) + solve(root.right, m)
        
        return solve(root, root.val)
