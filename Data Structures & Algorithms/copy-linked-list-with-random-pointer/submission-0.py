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
        d = {}
        temp = head
        if not head: return None
        while temp:
            node = Node(temp.val)
            d[temp] = node
            temp = temp.next
        temp = head
        res = d[temp]
        while temp:
            cur = d[temp]
            cur.next = d.get(temp.next, None)
            cur.random = d.get(temp.random, None)
            temp = temp.next
        return res
        
        
        