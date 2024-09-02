"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def solve(node, lst):
            if node is None:
                return None
            for child in node.children:
                solve(child, lst)
            lst.append(node.val)
        ans = []
        solve(root, ans)
        return ans
