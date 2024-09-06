# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        # Find the head of the new list
        while head.val in nums:
            head = head.next

        # Now remove nodes
        curr = head
        while curr is not None:
            while curr.next is not None and curr.next.val in nums:
                curr.next = curr.next.next
            curr = curr.next
        return head
