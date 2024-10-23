# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Basically copied from no. 2583
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

        root.val = 0
        neighbours = set()
        neighbours.add(root)

        k = 1
        while k < n:
            target = sums[k]
            new_set = set()
            for neigh in neighbours:
                tot = 0
                if neigh.left is not None:
                    tot += neigh.left.val
                    new_set.add(neigh.left)
                if neigh.right is not None:
                    tot += neigh.right.val
                    new_set.add(neigh.right)
                if neigh.left is not None:
                    neigh.left.val = target - tot
                if neigh.right is not None:
                    neigh.right.val = target - tot
            k += 1
            neighbours = new_set

        return root
