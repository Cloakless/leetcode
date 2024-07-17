# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        trees = []
        deletions = set(to_delete)

        def process(node, is_root):
            if node is None:
                return None
            left = node.left
            right = node.right
            if node.val not in deletions and is_root:
                trees.append(node)
            if node.val in deletions:
                base_root = True
            else:
                base_root = False
            if left and left.val in deletions:
                node.left = None
            if right and right.val in deletions:
                node.right = None
            process(left, base_root)
            process(right, base_root)
            return None

        process(root, True)
        return trees
