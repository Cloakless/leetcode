# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def create_tree(nodes, post_nodes):
            if len(nodes) == 0:
                return None
            root = TreeNode(nodes[0])
            if len(nodes) == 1:
                return root
            elif len(nodes) == 2:
                root.left = TreeNode(nodes[1])
                return root
            l_root = nodes[1]
            for i in range(len(post_nodes)):
                if post_nodes[i] == l_root:
                    l_pre, l_post = nodes[1:i+2], post_nodes[:i+1]
                    r_pre, r_post = nodes[i+2:], post_nodes[i+1:-1]
                    root.left = create_tree(l_pre, l_post)
                    root.right = create_tree(r_pre, r_post)
                    break
            return root
        return create_tree(preorder, postorder)
