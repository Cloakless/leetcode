# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def follow_path(path):
            curr_node = root
            string = ""
            for i in range(1, len(path)):
                if curr_node.left:
                    if curr_node.left.val == path[i]:
                        curr_node = curr_node.left
                        string += 'L'
                        continue
                curr_node = curr_node.right
                string += 'R'
            return string

        def find(val, root, path):
            if root is None:
                return None
            path.append(root.val)
            if root.val == val:
                return path
            else:
                first = find(val, root.left, path)
                if first:
                    return first
                last = find(val, root.right, path)
                if last:
                    return last
                path.pop()
                return None
        lpath, rpath = find(startValue, root, []), find(destValue, root, [])
        m, n = len(lpath), len(rpath)
        if m <= n:
            for i in range(m):
                if lpath[i] != rpath[i]:
                    shared = i-1
                    break
            if lpath[m - 1] == rpath[m - 1]:
                shared = m - 1
        else:
            for i in range(n):
                if lpath[i] != rpath[i]:
                    shared = i-1
                    break
            if lpath[n - 1] == rpath[n - 1]:
                shared = n - 1
        directions = ""
        if shared < m:
            directions += 'U'*(m - shared - 1)
        directions += follow_path(rpath)[shared:]
        return directions
