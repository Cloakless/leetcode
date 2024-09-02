# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def total(node, acc):
            base = 10*acc + node.val
            tot = 0
            if node.left is None and node.right is None:
                tot += base
            if node.right is not None:
                tot += total(node.right, base)
            if node.left is not None:
                tot += total(node.left, base)
            return tot
        return total(root, 0)
