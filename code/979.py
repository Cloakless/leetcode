# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tot = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return node.left is None and node.right is None
        def balance(node):
            if node is None:
                return 0
            left_sum = balance(node.left)
            right_sum = balance(node.right)
            if left_sum < 0:
                Solution.tot += -1*left_sum
            if right_sum < 0:
                Solution.tot += -1*right_sum
            
            node.val += left_sum + right_sum
            surplus = node.val - 1
            if surplus > 0:
                Solution.tot += surplus
            return surplus
        balance(root)
        ans = Solution.tot
        Solution.tot = 0 # Yes I have to reset this between function calls...
        return ans
