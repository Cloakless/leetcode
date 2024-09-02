# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def prune(node):
            if node.left is not None:
                node.left = prune(node.left)
            if node.right is not None:
                node.right = prune(node.right)       
            if node.right is None and node.left is None:
                if node.val == target:
                    return None
            return node
        return prune(root)

