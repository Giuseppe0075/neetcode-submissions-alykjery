# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        max_depth = -1
        def solve(root, d):
            if not root:
                return
            nonlocal ans
            nonlocal max_depth
            if d > max_depth:
                ans.append(root.val)
                max_depth = d
            solve(root.right, d+1)
            solve(root.left, d+1)
            return
        solve(root, 0)
        return ans