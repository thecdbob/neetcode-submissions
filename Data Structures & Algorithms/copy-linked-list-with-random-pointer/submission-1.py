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
        copyList = {None: None}
        current = head
        while current:
            copyList[current] = Node(current.val, None, None)
            current = current.next
        current = head
        while current:
            copyList[current].next = copyList[current.next]
            copyList[current].random = copyList[current.random]
            current = current.next
        return copyList[head]