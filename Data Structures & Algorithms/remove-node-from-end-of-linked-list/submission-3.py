# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0
        tmp = head
        while tmp:
            m += 1
            tmp = tmp.next

        n = m - n
        if n == 0:
            return head.next
        
        prev = curr = head
        for i in range(n):
            curr = curr.next
            if i == 0: continue
            prev = prev.next
        prev.next = curr.next
        return head
        
        