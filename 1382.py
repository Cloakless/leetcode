# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def collectNodes(root, nodes):
            nodes.append(root.val)
            if root.right:
                collectNodes(root.right, nodes)
            if root.left:
                collectNodes(root.left, nodes)

        def constructTree(nodes):
            if not nodes:
                return None
            mid = len(nodes)//2
            return TreeNode(val=nodes[mid],
                            left=constructTree(nodes[:mid]),
                            right=constructTree(nodes[mid+1:]))

        collectNodes(root, nodes)
        return constructTree(sorted(nodes))
