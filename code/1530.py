# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def isLeaf(node):
            if node is None:
                return False
            return node.left is None and node.right is None

        def process(node):
            # Process each node, if it has two subtrees add all the pairs from each side
            nonlocal tot
            paths = []
            if node is None:
                return paths
            if isLeaf(node):
                paths.append(1)
                return paths
            lpaths, rpaths = process(node.left), process(node.right)
            for lpath in lpaths:
                for rpath in rpaths:
                    if lpath + rpath <= distance:
                        tot += 1
            for path in lpaths + rpaths:
                paths.append(path + 1)
            return paths

        tot = 0
        process(root)
        return tot
