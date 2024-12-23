# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def num_swaps(lst):
            tot = 0
            target = sorted(lst)
            pos = {}

            for idx, val in enumerate(lst):
                pos[val] = idx

            for i in range(len(lst)):
                if lst[i] != target[i]:
                    tot += 1
                    curr_pos = pos[target[i]]
                    pos[lst[i]] = curr_pos
                    lst[curr_pos] = lst[i]
            return tot

        nodes = [root]
        ans = 0
        while nodes:
            vals = []
            children = []
            for node in nodes:
                vals.append(node.val)
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
            ans += num_swaps(vals)
            nodes = children
        return ans
