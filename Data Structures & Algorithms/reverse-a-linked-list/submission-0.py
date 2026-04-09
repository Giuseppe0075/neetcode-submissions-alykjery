# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        prec = None
        nextNode = head.next
        while nextNode is not None:
            head.next = prec
            prec = head
            head = nextNode
            nextNode = head.next
        head.next = prec
        return head

        #None<-0-<1<-2->3
        #            p  H  n