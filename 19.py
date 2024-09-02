# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        last = head
        i = 1
        while i < n:
            last = last.next
            i += 1
        if last.next is None:
            return first.next
        while last.next is not None:
            last = last.next
            if last.next is None:
                first.next = first.next.next
                return head
            first = first.next
