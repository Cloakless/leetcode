# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if a > b:
                a,b = b,a
            if a == 0:
                return b
            if b == a + 1:
                return 1
            return gcd(b-a,a)
        curr = head
        while curr.next != None:
            sub = curr.next
            curr.next = ListNode(val=gcd(curr.val, sub.val), next=sub)
            curr = sub
        return head
        
