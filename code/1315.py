# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        tot = 0
        def process(node, parent, grandparent):
            nonlocal tot
            if grandparent % 2 == 0:
                tot += node.val
            if node.left is not None:
                process(node.left, node.val, parent)
            if node.right is not None:
                process(node.right, node.val, parent)
        
        process(root, -1, -1)
        return tot
        
