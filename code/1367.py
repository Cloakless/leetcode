# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def pathFromHere(head, root):
            if head is None:
                return True
            if root is None:
                return head is None
            if head.val != root.val:
                return False
            return pathFromHere(head.next, root.left) or pathFromHere(head.next, root.right)
        # Base case
        if head is None:
            return True
        if root is None:
            return head is None

        # Recurse
        is_left = False
        is_right = False
        starts_here = False
        starts_here = pathFromHere(head, root)
        if starts_here:
            return True
        is_left = self.isSubPath(head, root.left)
        if is_left:
            return True
        is_right = self.isSubPath(head, root.right)
        if is_right:
            return True
        return False
    
