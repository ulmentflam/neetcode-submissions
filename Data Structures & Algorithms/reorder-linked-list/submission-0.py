# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverse = slow.next 
        previous = slow.next = None
        while reverse:
            tmp, reverse.next = reverse.next, previous
            previous, reverse = reverse, tmp
        
        first, reverse = head, previous
        while reverse:
            tmp_1, tmp_2 = first.next, reverse.next
            first.next, reverse.next = reverse, tmp_1
            first, reverse = tmp_1, tmp_2
        