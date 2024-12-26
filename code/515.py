# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        neighs = set()
        neighs.add(root)
        while neighs:
            best = None
            children = set()
            for cand in neighs:
                if cand.left is not None:
                    children.add(cand.left)
                if cand.right is not None:
                    children.add(cand.right)
                if best is None:
                    best = cand.val
                else:
                    best = max(best, cand.val)
            ans.append(best)
            neighs = children
        return ans
        
