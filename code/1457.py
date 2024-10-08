# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        import copy
        paths = []
        def find_paths(node, counter):
            nc = copy.deepcopy(counter)
            nc[node.val] += 1
            if node.left is not None:
                find_paths(node.left, nc)
            if node.right is not None:
                find_paths(node.right, nc)
            if node.left is None and node.right is None:
                paths.append(nc)
                return

        def is_pseudo(path):
            num_odds = 0
            for thing in path:
                if path[thing] % 2 == 1 and num_odds == 0:
                    num_odds = 1
                elif path[thing] % 2 == 0:
                    continue
                else:
                    return False
            return True

        find_paths(root, defaultdict(int))
        print(paths)
        ans = sum([is_pseudo(path) for path in paths])
        return ans
        
