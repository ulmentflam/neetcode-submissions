# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q = deque([p])
        q_q = deque([q])

        while p_q and q_q:
            for _ in range(len(p_q)):
                node_p = p_q.popleft()
                node_q = q_q.popleft()

                if node_p is None and node_q is None:
                    continue
                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False
                p_q.append(node_p.left)
                p_q.append(node_p.right)
                q_q.append(node_q.left)
                q_q.append(node_q.right)
        
        return True
        