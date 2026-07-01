# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        #reverse 2nd half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        h1 = head
        h2 = prev
        while h2:
            temp = h1.next
            temp2 = h2.next
            h1.next = h2
            h2.next = temp
            h1 = temp
            h2= temp2

