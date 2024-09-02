# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def solve(node, lst):
            if node is None:
                return None
            solve(node.left, lst)
            solve(node.right, lst)
            lst.append(node.val)
        ans = []
        solve(root, ans)
        return ans
