# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        cur = new_head
        n = 0
        
        while cur.next:
            if n == 0:
                h1 = cur
            
            cur = cur.next
            n += 1
            
            if n == k:
                temp_head = h1
                temp_tail = h1.next
                
                group_next = cur.next 
                
                prec = group_next     
                
                curr_rev = temp_head.next 
                
                while curr_rev != group_next:
                    succ = curr_rev.next
                    curr_rev.next = prec
                    prec = curr_rev
                    curr_rev = succ
                
                temp_head.next = prec
                
                cur = temp_tail
                n = 0
        return new_head.next