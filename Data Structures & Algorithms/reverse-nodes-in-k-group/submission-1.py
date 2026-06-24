# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def get_kth(self, node: ListNode, k: int) -> ListNode:
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        
        while True:
            kth = self.get_kth(prev_group, k)
            if not kth:
                break
            next_group = kth.next

            prev, curr = kth.next, prev_group.next
            while curr != next_group: 
                tmp, curr.next = curr.next, prev
                prev, curr = curr, tmp
            
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp
        return dummy.next
            