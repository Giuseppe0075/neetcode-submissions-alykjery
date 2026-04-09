"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        d = {None: None}
        while curr:
            node = Node(curr.val)
            d[curr] = node
            curr = curr.next

        new_head = curr = d[head]
        while head:
            curr.next = d[head.next]
            curr.random = d[head.random]
            curr = curr.next
            head = head.next

        return new_head

