# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced_dfs(root: Optioal[TreeNode]) -> Tuple(bool, int):
            if not root:
                return True, 0
            
            left, right = balanced_dfs(root.left), balanced_dfs(root.right)
            left_balanced, left_depth = left
            right_balanced, right_depth = right
            balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
            return balanced, 1 + max(left_depth, right_depth)
        
        balanced, _ = balanced_dfs(root)
        return balanced
        