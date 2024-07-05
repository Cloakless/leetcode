# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_crit(a, b, c):
            return (a > b and b < c) or (a < b and b > c)
        # Find first critical point
        left = head
        current = head.next
        right = current.next
        first_point = None
        diff = None
        position = 1
        best = 100000
        while right is not None:
            if is_crit(left.val, current.val, right.val):
                first_point = position
                last_point = position
                break
            position += 1
            left, current, right = left.next, current.next, right.next
        
        if first_point is None:
            return [-1,-1]

        left, current, right = left.next, current.next, right.next
        position += 1
        while right is not None:
            if is_crit(left.val, current.val, right.val):
                best = min(best, position - last_point)
                last_point = position                
            left, current, right = left.next, current.next, right.next
            position += 1
        if first_point == last_point:
            return [-1, -1]
        return [best, last_point - first_point]
