# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first, second = dummy, dummy
        i = 0
        while i < n and second:
            second = second.next
            i+= 1
        while second:
            prev = first
            first = first.next
            second = second.next
        prev.next = first.next
        return dummy.next