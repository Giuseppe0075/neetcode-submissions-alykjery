# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            if head is None:
                head = node
                curr = head
                continue
            curr.next = node
            curr = curr.next
        if list1 is not None:
            if head is None:
                head = list1
            else:
                curr.next = list1
        elif list2 is not None:
            if head is None:
                head = list2
            else:
                curr.next = list2
            
        return head
