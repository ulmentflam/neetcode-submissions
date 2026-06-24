# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        group = 0
        
        while current and group < k:
            current = current.next
            group += 1
        
        if group == k:
            current = self.reverseKGroup(current, k)
            while group > 0:
                tmp = head.next
                head.next = current
                current = head
                head = tmp
                group -= 1
            head = current
        return head