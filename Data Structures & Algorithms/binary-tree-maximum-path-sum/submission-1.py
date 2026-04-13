# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float("-inf")
        def dfs(node):
            if not node:
                return 0
            nonlocal ans

            left_sum = dfs(node.left)
            if left_sum < 0:
                left_sum = 0
            right_sum = dfs(node.right)
            if right_sum < 0:
                right_sum = 0
            left_to_right_sum = left_sum + node.val + right_sum
            
            if ans < left_to_right_sum:
                ans = left_to_right_sum
            return max(left_sum, right_sum) + node.val

        dfs(root)
        return ans
