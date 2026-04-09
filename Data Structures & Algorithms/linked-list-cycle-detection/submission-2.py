# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow.next and fast.next:
            fast = fast.next.next
            if fast == None:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False