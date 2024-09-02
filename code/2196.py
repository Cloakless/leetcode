# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = {}
        ps = set()
        cs = set()
        for node in descriptions:
            ps.add(node[0])
            cs.add(node[1])
            if node[0] not in children:
                children[node[0]] = [(node[1], node[2])]
            else:
                children[node[0]].append((node[1], node[2]))
        for p in ps:
            if p not in cs:
                root = TreeNode(p)
                break
        def createTree(node):
            for child in children[node.val]:
                if child[1] == 1:
                    node.left = TreeNode(val=child[0])
                    if child[0] in ps:
                        createTree(node.left)
                else:
                    node.right = TreeNode(val=child[0])
                    if child[0] in ps:
                        createTree(node.right)
        createTree(root)
        return root
