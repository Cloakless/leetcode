# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def search(node):
            tot = 0
            if node.val is None:
                return 0
            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    tot += node.left.val
                tot += search(node.left)
            if node.right is not None:
                tot += search(node.right)
            return tot
        return search(root)
        
