class Solution:
    def maxDepth(self, s: str) -> int:
        dep = 0
        max_dep = 0
        for elem in s:
            if elem == "(":
                dep += 1
                if dep > max_dep:
                    max_dep = dep
            elif elem == ")":
                dep -= 1
        return max_dep
        
