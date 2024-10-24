# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def is_flip_equiv(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None and r2 is not None:
                return False
            if r2 is None and r1 is not None:
                return False
            # They are both not None
            if r1.val != r2.val:
                return False
            if (is_flip_equiv(r1.left, r2.left) and is_flip_equiv(r1.right, r2.right)) or (is_flip_equiv(r1.left, r2.right) and is_flip_equiv(r1.right, r2.left)):
                return True
            return False

        return is_flip_equiv(root1, root2)
