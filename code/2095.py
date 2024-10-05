# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        num = 0
        while curr != None:
            curr = curr.next
            num += 1
        target = num // 2
        if target == 0:
            return None
        elif num == 2:
            head.next = None
            return head
        else:
            ind = 0
            curr = head
            while ind < target - 1:
                curr = curr.next
                ind += 1
            temp = curr.next
            curr.next = curr.next.next
            del temp
            return head
