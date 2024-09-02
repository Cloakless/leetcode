# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def shortest_string(a, b):
            alist = list(a)
            blist = list(b)
            if len(a) < len(b):
                shorter = a
            else:
                shorter = b
            for i in range(len(shorter)):
                if alist[i] < blist[i]:
                    return a
                elif blist[i] < alist[i]:
                    return b
            return shorter

        def search(node, so_far):
            new_far = so_far
            new_far += (node.val,)
            if node.left is None and node.right is None:
                # Leaf
                new_far = new_far[::-1]
                temp = []
                for j in range(len(new_far)):
                    temp.append(chr(int(new_far[j]) + 97))
                return "".join(temp)
            elif node.left is None and node.right is not None:
                return search(node.right, new_far)
            elif node.left is not None and node.right is None:
                return search(node.left, new_far)
            else:
                return shortest_string(search(node.left, new_far), search(node.right, new_far))
        return search(root, ())
