# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedHead = ListNode(-1)
        head1 = list1
        head2 = list2
        prev = mergedHead
        while head1 and head2:
            if head2.val > head1.val:
                prev.next = head1
                prev = head1
                head1 = head1.next
            else: 
                prev.next = head2
                prev = head2
                head2 = head2.next
        if head1:
            prev.next = head1
        else:
            prev.next = head2
        return mergedHead.next