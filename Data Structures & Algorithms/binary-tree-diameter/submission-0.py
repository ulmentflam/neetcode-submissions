# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0 # Simple dfs that accumulates the sum        
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal result

            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            result = max(result, left + right)
            return 1 + max(left,right)
        dfs(root)
        return result

                