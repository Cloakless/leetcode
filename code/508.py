# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        subtree_sums = defaultdict(int)
        def process(node):
            val = node.val
            if node.left is not None:
                val += process(node.left)
            if node.right is not None:
                val += process(node.right)
            subtree_sums[val] += 1
            return val
        
        process(root)
        vals = []
        for option in subtree_sums:
            vals.append((subtree_sums[option], option))
        vals.sort(reverse=True)
        ans = [vals[0][1]]
        for i in range(1, len(vals)):
            if vals[i][0] == vals[0][0]:
                ans.append(vals[i][1])
            else:
                return ans
        return ans
        
