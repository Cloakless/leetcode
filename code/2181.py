# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        child = current.next
        new_head = current
        while child.next != None:
            if child.val == 0:
                current.next = child.next
                current = current.next
                child = current.next
            else:
                current.val += child.val
                child = child.next
        current.next = None
        return new_head
