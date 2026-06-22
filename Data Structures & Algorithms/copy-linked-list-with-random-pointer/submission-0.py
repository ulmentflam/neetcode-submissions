"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_copy: dict[Node, Node] = {None: None}

        # Store new links in a hashmap
        current = head
        while current:
            copy = Node(current.val)
            original_copy[current] = copy
            current = current.next
        

        # Correct the link pointers
        current = head
        while current:
            copy = original_copy[current]
            copy.next = original_copy[current.next]
            copy.random = original_copy[current.random]
            current = current.next
            
        return original_copy[head]

        