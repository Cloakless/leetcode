# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        def find_dashes(string, k):
            pattern = re.compile('-' * k + r'[^-]')
            matches = [match.start() for match in pattern.finditer(string)]
            return [idx + k for idx in matches if idx == 0 or string[idx-1] != '-']

        def process(string):
            # Get root
            first_num = int(string.split('-')[0])
            root = TreeNode(first_num)
            if '-' not in string:
                return root
            i = 0
            offset = len(str(first_num))
            while string[offset+i] == '-':
                i += 1
            str_idxs = find_dashes(string, i)
            if len(str_idxs) == 1:
                root.left = process(string[str_idxs[0]:])
            elif len(str_idxs) == 2:
                root.left = process(string[str_idxs[0]:str_idxs[1]-i])
                root.right = process(string[str_idxs[1]:])


            return root
        return process(traversal)



        
