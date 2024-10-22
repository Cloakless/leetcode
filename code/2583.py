# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        neighbours = set()
        neighbours.add(root)
        while neighbours:
            tot = 0
            next_set = set()
            for neigh in neighbours:
                tot += neigh.val
                if neigh.right is not None:
                    next_set.add(neigh.right)
                if neigh.left is not None:
                    next_set.add(neigh.left)
            sums.append(tot)
            neighbours = next_set
        n = len(sums)
        if n < k:
            return -1
        sums.sort()
        return sums[n-k]
