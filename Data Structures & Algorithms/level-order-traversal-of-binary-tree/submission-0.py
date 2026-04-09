# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def solve(root, d):
            nonlocal ans
            if not root:
                return
            if len(ans) <= d:
                ans.append([])
            ans[d].append(root.val)
            solve(root.left, d+1)
            solve(root.right, d+1)
            return
        solve(root, 0)
        return ans