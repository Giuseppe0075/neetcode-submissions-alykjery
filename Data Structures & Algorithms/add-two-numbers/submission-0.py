# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        riporto = 0
        somma = 0
        head = curr = ListNode()
        while l1 and l2:
            somma = l1.val + l2.val + riporto
            riporto = int(somma / 10)
            if riporto > 0:
                somma -= 10
            curr.next = ListNode(somma)

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            somma = l1.val + riporto
            riporto = int(somma / 10)
            if riporto > 0:
                somma -= 10
            curr.next = ListNode(somma)
            curr = curr.next
            l1 = l1.next
        while l2:
            somma = l2.val + riporto
            riporto = int(somma / 10)
            if riporto > 0:
                somma -= 10
            curr.next = ListNode(somma)
            curr = curr.next
            l2 = l2.next
        if riporto > 0:
            curr.next = ListNode(riporto)
        return head.next
