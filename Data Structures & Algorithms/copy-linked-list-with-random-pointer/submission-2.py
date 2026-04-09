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
            tmp = Node(curr.val)
            d[curr] = tmp
            curr = curr.next

        curr = head
        while curr:
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            curr = curr.next
        return d[head]
        