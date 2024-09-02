# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evNode(node):
            if node.left is None:
                return bool(node.val)
            else:
                if node.val == 2:
                    return evNode(node.left) or evNode(node.right)
                else:
                    return evNode(node.left) and evNode(node.right)
        return evNode(root)
