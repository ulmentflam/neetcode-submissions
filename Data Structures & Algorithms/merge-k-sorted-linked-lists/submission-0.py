# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_list(self, list_1: ListNode, list_2: ListNode) -> ListNode:
        head = ListNode()
        tail = head
        while list_1 and list_2:
            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            tail = tail.next
        
        if list_1:
            tail.next = list_1
        if list_2:
            tail.next = list_2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                list_2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.merge_list(list_1, list_2))
            lists = merged_list
        return lists[0]
        