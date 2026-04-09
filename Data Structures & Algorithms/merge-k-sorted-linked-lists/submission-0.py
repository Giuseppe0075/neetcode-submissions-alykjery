# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        while True:
            minNode = -1
            minNodeValue = 0
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or minNodeValue > lists[i].val:
                    minNode = i
                    minNodeValue = lists[i].val
            if minNode == -1:
                break
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next
        return head.next
