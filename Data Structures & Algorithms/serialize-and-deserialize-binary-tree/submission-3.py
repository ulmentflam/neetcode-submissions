# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    NULL: str = "*"
    DELIM: str = ","
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return self.NULL
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                result.append(self.NULL)
                continue
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return self.DELIM.join(result)        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(self.DELIM)
        
        if vals[0] == self.NULL:
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        idx = 1
        while q:
            node = q.popleft()
            if vals[idx] != self.NULL:
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx += 1
            if vals[idx] != self.NULL:
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx += 1
        return root

        