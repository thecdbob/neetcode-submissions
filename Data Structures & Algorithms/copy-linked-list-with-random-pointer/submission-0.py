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
        listDict = {None: None}
        current = head
        while current:
            listDict[current] = Node(current.val, None, None)
            current = current.next
        current = head
        while current:
            listDict[current].next = listDict[current.next]
            listDict[current].random = listDict[current.random]
            current = current.next
        return listDict[head]