# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def convert(node, extra):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                node.val += extra
                return node.val - extra
            else:
                right_sum = convert(node.right, extra) + extra
                node.val += right_sum
                left_sum = convert(node.left, node.val)
                return left_sum + node.val - extra
        convert(root, 0)
        return root
