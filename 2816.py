# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def double(node):
            if node is None:
                return (None, 0)
            (rest, carry) = double(node.next)
            new_val = 2*node.val + carry
            rem = new_val % 10
            new_carry = int((new_val - rem)/10)
            node.val = rem
            return (node, new_carry)
            
        (head, carry) = double(head)
        if carry != 0:
            new_head = ListNode(val=carry, next=head)
            head = new_head
        return head
