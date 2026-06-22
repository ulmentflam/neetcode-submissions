# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        def get_len(n: ListNode) -> int:
            n_len = 0
            while n:
                n_len += 1
                n = n.next
            return n_len
        
        n_len = get_len(head)

        idx = n_len - n
        if idx <= 0:
            return head.next
        
        tmp = head
        i = 0
        while i <= idx:
            i += 1
            if i == idx:
                tmp.next = tmp.next.next
                return head
            tmp = tmp.next
        
        return head
        

        



        