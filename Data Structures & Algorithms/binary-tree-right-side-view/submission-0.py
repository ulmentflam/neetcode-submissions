# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS where we append the right value
        results = []
        q = deque([root])
        while q:
            right = None
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left) # We append left first so we don't traverse further left nodes
                    q.append(node.right)
            if right:
                results.append(right.val)
        return results
        