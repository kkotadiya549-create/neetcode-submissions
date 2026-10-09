# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # Recursively compute max downward path for subtrees, ignoring negative paths
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Update global max path sum including the current node as the highest point
            res = max(res, node.val + left_max + right_max)

            # Return maximum single-branch downward path to parent
            return node.val + max(left_max, right_max)

        dfs(root)
        return res