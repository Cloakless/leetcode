# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode()
            new_root.val = val
            new_root.left = root
            return new_root
        def add(node, num, depth):
            if depth > 2:
                if node.left:
                    add(node.left, num, depth-1)
                if node.right:
                    add(node.right, num, depth-1)
            else:
                # Add left
                old_left = node.left
                new_lnode = TreeNode()
                new_lnode.val = num
                new_lnode.left = old_left
                node.left = new_lnode

                # Add right
                old_right = node.right
                new_rnode = TreeNode()
                new_rnode.val = num
                new_rnode.right = old_right
                node.right = new_rnode
            return root
        return add(root, val, depth)
        
