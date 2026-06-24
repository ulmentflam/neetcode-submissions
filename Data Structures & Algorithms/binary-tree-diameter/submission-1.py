# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0 # Simple dfs that accumulates the sum        
        def dfs(self, root: Optional[TreeNode]) -> int:

            if not root: return 0
            left, right = dfs(self, root.left), dfs(self,root.right)
            self.result = max(self.result, left + right)
            return 1 + max(left,right)
        dfs(self, root)
        return self.result

                