# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listHeadPrev = ListNode()
        listTail = listHeadPrev
        while list1 and list2:
            if list1.val > list2.val:
                listTail.next = list2
                list2 = list2.next
            else:
                listTail.next = list1
                list1 = list1.next
            listTail = listTail.next
        if list1:
            listTail.next = list1
        elif list2:
            listTail.next = list2
        return listHeadPrev.next